import { createI18n } from 'vue-i18n'
import cs from './cs.json'

const i18n = createI18n({
    legacy: false,
    locale: "cs",
    messages: {
        cs: cs,
    },
    datetimeFormats: {
        cs: {
            short: {
                year: "numeric",
                month: 'numeric',
                day: 'numeric',
                hour: '2-digit',
                minute: '2-digit',
            },
            dateOnly: {
                year: "numeric",
                month: 'numeric',
                day: 'numeric',
            },
        },
    },
})

export default i18n