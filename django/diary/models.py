from datetime import datetime, date
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models import Sum, F
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


User = get_user_model()


class ProjectStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="statuses")
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, null=True, blank=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="units")
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="projects")
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    start_date = models.DateField(default=timezone.now, null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.ForeignKey(ProjectStatus, on_delete=models.SET_NULL, null=True, blank=True, related_name="projects")
    slug = models.SlugField(max_length=120, null=True, blank=True)

    class Meta:
        ordering = ["-start_date", "name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk:
            origin = Project.objects.get(pk=self.pk)
            if origin.name != self.name:
                self.slug = slugify(self.name)
        else:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    # @property
    # def total_cost(self):
    #     """
    #     Updates total project costs based on materials used in daily records.
    #     """
    #     return (
    #             self.daily_logs.aggregate(
    #                 total=Sum(
    #                     F("daily_usages__used_quantity") * F("daily_usages__material__price_per_unit")  # upravit
    #                 )
    #             )["total"] or 0
    #     )

    # @property
    # def total_work_time(self):
    #     """
    #     Calculates the total working time from all daily entries
    #     """
    #     total_time = self.daily_logs.aggregate(total=Sum("work_time"))["total"]
    #     return total_time or timedelta(0)


class DailyLog(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name="daily_logs")
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(default=timezone.now)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    work_time = models.DurationField(null=True, blank=True)
    temperature = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ["-date", "-start_time"]

    def __str__(self):
        return f"{self.date} - {self.project.name}"

    def save(self, *args, **kwargs):
        if self.start_time and self.end_time:
            self.work_time = (
                datetime.combine(date.min, self.end_time)
                - datetime.combine(date.min, self.start_time)
            )
        super().save(*args, **kwargs)

    @property
    def user(self):
        return self.project.user


class Material(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="materials")
    name = models.CharField(max_length=100)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True, related_name="materials")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"

    @property
    def stock(self):
        adds = self.purchases.aggregate(total=Sum("quantity"))["total"] or 0
        usages = self.material_usages.aggregate(total=Sum("used_quantity"))["total"] or 0
        return adds - usages

class MaterialUsage(models.Model):
    daily_log = models.ForeignKey(DailyLog, on_delete=models.CASCADE, related_name="daily_usages")
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="material_usages")
    used_quantity = models.PositiveSmallIntegerField()
    used_at = models.DateField()

    class Meta:
        ordering = ["-used_at"]

    def __str__(self):
        return f"{self.daily_log.date.strftime('%Y-%m-%d')} - {self.material.name} {self.used_quantity}"

    def clean(self):
        if self.used_quantity > (self.material.stock or 0):
            raise ValidationError("Insufficient amount of material in stock.")

    def save(self, *args, **kwargs):
        if not self.used_at:
            self.used_at = self.daily_log.date
        super().save(*args, **kwargs)


class MaterialPurchase(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="purchases")
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    price_per_unit = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    buy_at = models.DateField()

    class Meta:
        ordering = ["-buy_at"]

    def __str__(self):
        return f"{self.material.name} ({self.quantity} {self.material.unit.name if self.material.unit else ''})"

    def save(self, *args, **kwargs):
        if self.quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        if not self.price_per_unit:
            self.price_per_unit = self.price / self.quantity
        super().save(*args, **kwargs)
