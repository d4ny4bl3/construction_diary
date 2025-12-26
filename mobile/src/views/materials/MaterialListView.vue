<template>
	<IonPage>
		<IonHeader>
			<IonToolbar>
				<IonButtons slot="start">
					<IonMenuButton />
				</IonButtons>
				<IonTitle class="ion-text-center">Materiály</IonTitle>
			</IonToolbar>
		</IonHeader>

		<IonContent>
			<IonCard>
				<IonCardContent>

					<IonGrid class="table-header">
						<IonRow>
							<IonCol size="6" class="fw-bold ion-text-center">Název</IonCol>
							<IonCol size="6" class="fw-bold ion-text-center">Skladem</IonCol>
						</IonRow>
					</IonGrid>

					<IonGrid>
						<IonRow class="table-row">
							<IonCol size="6" class="ion-text-center">Data A1</IonCol>
							<IonCol size="6" class="ion-text-center">Data B1</IonCol>
						</IonRow>

						<IonRow class="table-row">
							<IonCol size="6" class="ion-text-center">Data A2</IonCol>
							<IonCol size="6" class="ion-text-center">Data B2</IonCol>
						</IonRow>
					</IonGrid>

				</IonCardContent>
			</IonCard>

			<IonFab vertical="bottom" horizontal="end" slot="fixed" class="fab_offset">
				<IonFabButton>
					<IonIcon :icon="addOutline" />
				</IonFabButton>
			</IonFab>
		</IonContent>
	</IonPage>
</template>

<script>
import {
	IonButtons,
	IonCard,
	IonCardContent,
	IonContent,
	IonHeader,
	IonMenuButton,
	IonPage,
	IonTitle,
	IonToolbar,
	IonGrid,
	IonRow,
	IonCol,
	IonFab,
	IonFabButton,
	IonIcon,
} from '@ionic/vue';

import {
	addOutline,
} from 'ionicons/icons'

export default {
	name: "MaterialListView",
	components: {
		IonButtons,
		IonCard,
		IonCardContent,
		IonContent,
		IonHeader,
		IonMenuButton,
		IonPage,
		IonTitle,
		IonToolbar,
		IonGrid,
		IonRow,
		IonCol,
		IonFab,
		IonFabButton,
		IonIcon,
	},
	data() {
		return {
			addOutline,
		}
	}
}
</script>

<style scoped>
.table-header {
  border-bottom: 2px solid var(--ion-color-light);
  margin-bottom: 8px;
  font-weight: bold;
}

.table-row {
  border-bottom: 1px solid var(--ion-color-light);
  padding: 6px 0;
}

.table-row:last-child {
  border-bottom: none;
}

.fab_offset {
	--ion-safe-area-bottom: 10px;
	margin-bottom: 10px;
	margin-right: 10px;
}
</style>