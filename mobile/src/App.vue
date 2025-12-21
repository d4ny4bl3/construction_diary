<template>
  <IonApp>
    <IonMenu content-id="main-content">
      <IonHeader>
        <IonToolbar>
          <IonTitle>Menu</IonTitle>
        </IonToolbar>
      </IonHeader>

      <IonContent>
        <IonList>
          <IonItem router-link="/a">A</IonItem>
          <IonItem router-link="/b">B</IonItem>
        </IonList>
      </IonContent>
    </IonMenu>

    <IonRouterOutlet id="main-content" />
  </IonApp>
</template>

<script setup>
import {
  IonApp,
  IonMenu,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonContent,
  IonList,
  IonItem,
  IonRouterOutlet,
} from '@ionic/vue'
</script>

<style scoped></style>
