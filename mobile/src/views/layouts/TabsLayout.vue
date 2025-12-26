<template>
	<IonPage>
		<IonTabs>
			<IonRouterOutlet />

			<IonTabBar slot="bottom">
				<IonTabButton tab="dashboard" href="/dashboard">
					<IonIcon :icon="homeOutline" />
					<IonLabel>Přehledy</IonLabel>
				</IonTabButton>

				<IonTabButton tab="projects" href="/projects">
					<IonIcon :icon="constructOutline" />
					<IonLabel>Projekty</IonLabel>
				</IonTabButton>

				<IonTabButton tab="materials" href="/materials">
					<IonIcon :icon="cubeOutline" />
					<IonLabel>Materiály</IonLabel>
				</IonTabButton>
			</IonTabBar>
		</IonTabs>
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
} from '@ionic/vue';

import {
	homeOutline,
	constructOutline,
	cubeOutline,
} from 'ionicons/icons';

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
    },
    data() {
        return {
            homeOutline,
            constructOutline,
			cubeOutline,
        }
    }
}
</script>