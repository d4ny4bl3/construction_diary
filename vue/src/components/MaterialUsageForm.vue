<template>
    <div class="row align-items-end g-3 w-100">
        <div class="col-5">
            <label for="usedAt" class="form-label fw-bold">{{ t("materialUsage.date") }}</label>
            <input type="date" class="form-control" v-model="usedAt">
        </div>

        <div class="col-5">
            <label for="material" class="form-label fw-bold">{{ t("materialUsage.label") }}</label>
            <select class="form-select" v-model="material" required>
                <option
                    v-for="material in materials"
                    :key="material.id"
                    :value="material.id"
                >
                    {{ material.name }}
                </option>
            </select>
        </div>

        <div class="col-2">
            <label for="quantity" class="form-label fw-bold">{{ t("materialUsage.usedQuantity") }}</label>
            <input
                type="number"
                class="form-control"
                min="1"
                :max="availableStock"
                v-model.number="quantity"
                :class="{ 'is-invalid': isQuantityInvalid }"
                required
            >
            <div v-if="isQuantityInvalid" class="invalid-feedback">
                {{ $t("materialUsage.availableOnly") }} {{ availableStock }} {{ selectedMaterial?.unit?.name || "" }}
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useI18n } from 'vue-i18n';
import { useMaterialStore } from '@/stores/materialStore';

const props = defineProps({
    materials: Array,
    submitLabel: {
        type: String,
        default: ""
    }
})

const emit = defineEmits(["submit"])
const storeMaterial = useMaterialStore()
const { t } = useI18n()

onMounted(async () => {
    try {
        await storeMaterial.fetchMaterials()
    } catch (error) {
        console.error("Error loading materials.", error)
    }
})

const material = ref("")
const usedAt = ref("")
const quantity = ref(null)

const selectedMaterial = computed(() => {
    return props.materials.find(m => m.id === material.value)
})

const availableStock = computed(() => {
    return selectedMaterial.value ? selectedMaterial.value.stock : null
})

const isQuantityInvalid = computed(() => {
    if (!quantity.value || !availableStock.value) return false
    return quantity.value > availableStock.value
})

const getData = () => ({
    material: material.value,
    used_at: usedAt.value,
    used_quantity: quantity.value
})

defineExpose({ getData })
</script>