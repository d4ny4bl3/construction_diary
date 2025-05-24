<template>
    <form class="row g-3 p-3" ref="form" @submit.prevent="submit">
        <div class="col-6">
            <label for="name" class="form-label fw-bold">{{ t("material.name") }}</label>
            <input type="text" class="form-control" id="name" v-model="name" required>
        </div>
        <div class="col-6">
            <label for="unit" class="form-label fw-bold">{{ t("material.unit") }}</label>
            <select class="form-select" v-model="unit" required>
                <option
                    v-for="unit in store.units"
                    :key="unit.id"
                    :value="unit.id"
                >
                    {{ unit.name }}
                </option>
            </select>
        </div>

        <div class="my-4">
            <button type="submit" class="btn btn-primary w-100 py-3 fw-bold fs-5 text-white">{{ label }}</button>
        </div>
    </form>
</template>

<script setup>
import { useMaterialStore } from '@/stores/materialStore';
import { ref, watch, computed, onMounted } from 'vue';
import { useI18n } from 'vue-i18n';

const props = defineProps({
    material: {
        type: Object,
        default: null
    },
    submitLabel: {
        type: String,
        default: ""
    }
})
const emit = defineEmits(["submit"])

const store = useMaterialStore()
const { t } = useI18n()

onMounted(async () => {
    try {
        await store.fetchUnits()
    } catch (error) {
        console.error("Error loading units.", error)
    }
})

const name = ref("")
const unit = ref("")
const label = computed(() =>
    props.submitLabel || t("utils.create")
)

watch(() => props.material,
    (newVal) => {
        if (newVal) {
            name.value = newVal.name || ""
            unit.value = newVal.unit?.id || ""
        }
    },
    { immediate: true }
)

const submit = () => {
    emit("submit", {
        name: name.value,
        unit: unit.value
    })
}
</script>