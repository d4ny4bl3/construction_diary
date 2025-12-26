<template>
	<IonPage>
		<IonHeader>
			<IonToolbar>
				<IonButtons slot="start">
					<IonMenuButton />
				</IonButtons>
				<IonTitle>Nastavení</IonTitle>
			</IonToolbar>
		</IonHeader>

		<IonContent class="ion-padding">
			<IonList>
				<IonItem>
					<IonLabel>Jednotky</IonLabel>
				</IonItem>

				<IonItem>
					<IonLabel>Statusy projektů</IonLabel>
				</IonItem>

				<IonItem>
					<IonLabel>Změna hesla</IonLabel>
				</IonItem>
			</IonList>
		</IonContent>
	</IonPage>
</template>

<script>
import {
	IonButtons,
	IonContent,
	IonHeader,
	IonItem,
	IonLabel,
	IonList,
	IonMenuButton,
	IonPage,
	IonTitle,
	IonToolbar,
} from '@ionic/vue';

export default {
	name: "SettingsView",
	components: {
		IonButtons,
		IonContent,
		IonHeader,
		IonItem,
		IonLabel,
		IonList,
		IonMenuButton,
		IonPage,
		IonTitle,
		IonToolbar,
	}
}
</script>