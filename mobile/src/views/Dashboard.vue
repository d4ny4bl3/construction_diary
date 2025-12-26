<template>
    <IonPage>
        <IonHeader>
            <IonToolbar>
                <IonButtons slot="start">
                    <IonMenuButton />
                </IonButtons>
                <IonTitle>Přehledy</IonTitle>
            </IonToolbar>
        </IonHeader>

        <IonContent class="ion-padding ion-text-center">
            <IonText>
                Dashboard
            </IonText>
        </IonContent>
    </IonPage>
</template>

<script>
import {
    IonPage,
    IonHeader,
    IonToolbar,
    IonButtons,
    IonMenuButton,
    IonTitle,
    IonContent,
    IonText,
} from '@ionic/vue'

export default {
    name: "Dashboard",
    components: {
        IonPage,
        IonHeader,
        IonToolbar,
        IonButtons,
        IonMenuButton,
        IonTitle,
        IonContent,
        IonText,
    }
}
</script>
