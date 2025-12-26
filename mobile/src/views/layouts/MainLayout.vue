<template>
    <IonPage>
        <IonMenu content-id="main-content">
            <IonHeader>
                <IonToolbar>
                    <IonTitle>Menu</IonTitle>
                </IonToolbar>
            </IonHeader>

            <IonContent>
                <IonList class="ion-padding">
                    <IonItem button @click="goTo('ProjectList')">Projekty</IonItem>
                    <IonItem button @click="goTo('MaterialList')">Materiály</IonItem>
                    <IonItem router-link="">Nákupy</IonItem>
                    <IonItem button @click="goTo('Settings')">Nastavení</IonItem>
                    <IonItem router-link="">Odhlásit</IonItem>
                </IonList>
            </IonContent>
        </IonMenu>

        <IonRouterOutlet id="main-content" />

    </IonPage>
</template>

<script>
import {
    IonPage,
    IonTabs,
    IonRouterOutlet,
    IonTabBar,
    IonTabButton,
    IonLabel,
    IonIcon,
    IonMenu,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent,
    IonList,
    IonItem,
} from '@ionic/vue';

import {
  gridOutline,
  constructOutline,
} from 'ionicons/icons';

import { menuController } from '@ionic/vue';

export default {
    name: "MainLayout",
    components: {
        IonPage,
        IonTabs,
        IonRouterOutlet,
        IonTabBar,
        IonTabButton,
        IonLabel,
        IonIcon,
        IonMenu,
        IonHeader,
        IonToolbar,
        IonTitle,
        IonContent,
        IonList,
        IonItem,
    },
    data() {
        return {
            gridOutline,
            constructOutline,
        }
    },
    methods: {
        async goTo(routeName) {
            await this.$router.push({ name: routeName })
            await menuController.close();
        }
    }
}
</script>