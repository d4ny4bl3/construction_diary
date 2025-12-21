<template>
    <IonPage>
        <IonTabs>
            <IonRouterOutlet />

            <IonTabBar slot="bottom">
                <IonTabButton tab="tab1" href="/tab1">
                    <IonLabel>Tab 1</IonLabel>
                </IonTabButton>

                <IonTabButton tab="tab2" href="/tab2">
                    <IonLabel>Tab 2</IonLabel>
                </IonTabButton>
            </IonTabBar>
        </IonTabs>
    </IonPage>
</template>

<script setup>
import {
    IonPage,
    IonTabs,
    IonRouterOutlet,
    IonTabBar,
    IonTabButton,
    IonLabel,
} from '@ionic/vue';

</script>