<template>
    <IonPage>
        <IonHeader>
            <IonToolbar>
                <IonButtons slot="start">
                    <IonMenuButton />
                </IonButtons>
                <IonTitle>Tab 2</IonTitle>
            </IonToolbar>
        </IonHeader>

        <IonContent class="ion-padding">
            Obsah Tab 2
        </IonContent>
    </IonPage>
</template>

<script setup>
import {
    IonPage,
    IonHeader,
    IonToolbar,
    IonButtons,
    IonMenuButton,
    IonTitle,
    IonContent,
} from '@ionic/vue'
</script>
