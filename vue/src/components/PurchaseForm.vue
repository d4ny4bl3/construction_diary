<template>
    <form class="row g-3 p-3" ref="form" @submit.prevent="submit">
        <div class="col-12 mb-2">
            <div class="row align-items-end">
                <div class="col-6">
                    <label for="material" class="form-label fw-bold">Materiál</label>
                    <select class="form-select" v-model="material" required>
                        <option
                            v-for="material in store.materials"
                            :key="material.id"
                            :value="material.id"
                        >
                            {{ material.name }}
                        </option>
                    </select>
                </div>

                <div class="col-4">
                    <label for="quantity" class="form-label fw-bold">Množství</label>
                    <input type="number" id="quantity" class="form-control" min="1" v-model="quantity" required>
                </div>

                <div class="col-2 pb-2">
                    <span class="fw-bold fs-5">{{ materialUnit }}</span>
                </div>
            </div>
        </div>
        <div class="col-6">
            <label for="price" class="form-label fw-bold">Cena</label>
            <input type="number" id="price" class="form-control" min="1" v-model="price" required>
        </div>
        <div class="col-6">
            <label for="pricePerUnit" class="form-label fw-bold">Cena za jednotku</label>
            <input type="number" id="pricePerUnit" class="form-control" :value="pricePerUnit" readonly>
        </div>
        <div class="col-6">
            <label for="buyAt" class="form-label fw-bold">Zakoupeno</label>
            <input type="date" class="form-control" v-model="buyAt" required>
        </div>


        <div class="my-4">
            <button type="submit" class="btn btn-primary w-100 py-3 fw-bold fs-5 text-white">{{ label }}</button>
        </div>
    </form>
</template>

<script setup>
import { useMaterialStore } from '@/stores/materialStore';
import { ref, watch, onMounted, computed } from 'vue';
import { useI18n } from 'vue-i18n';

const props = defineProps({
    purchase: {
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
        await store.fetchMaterials()
    } catch (error) {
        console.error("Error loading materials.", error)
    }
})

const material = ref("")
const materialUnit = computed(() => {
    const selected = store.materials.find(m => m.id === material.value)
    return selected?.unit?.name || ""
})

const quantity = ref("")
const price = ref("")
const buyAt = ref("")
const label = computed(() =>
    props.submitLabel || t("utils.create")
)
const pricePerUnit = computed(() => {
    const p = parseFloat(price.value)
    const q = parseFloat(quantity.value)
    if (!isNaN(p) && !isNaN(q) && q !== 0) {
        return (p / q).toFixed(2)
    }
    return ""
})

watch(() => props.purchase,
    (newVal) => {
        if (newVal) {
            material.value = newVal.material || null
            quantity.value = newVal.quantity || ""
            price.value = newVal.price || ""
            buyAt.value = newVal.buy_at || ""
        }
    },
    { immediate: true }
)

const submit = () => {
    emit("submit", {
        material: material.value,
        quantity: quantity.value,
        price: parseFloat(price.value),
        buyAt: buyAt.value,
    })
}
</script>