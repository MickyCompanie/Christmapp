import { getAllGroceries, getEmptyGrocerie, getSpecificGrocerie, createGrocerie, updateGrocerie, deleteGrocerie } from "../../service/grocerie";
import { useNotificationsStore } from "@/stores/notifications";
import router from "@/router"



export default {
    async getAllGroceriesAction() {
        return await getAllGroceries().then((res) => {
            this.groceries = res.data.groceries
            this.tableHeads = res.data.tableHeads
            this.attributes = res.data.attributes
        })
    },

    async resetGrocerieAction(){
        this.grocerie = null
    },

    async getEmptyGrocerieAction(){
        return await getEmptyGrocerie()
        .then((res) => {
            this.grocerie = res.data.grocerie
            this.persons = res.data.persons
            this.statuses = res.data.statuses
        })
    },

    async getSpecificGrocerieAction(payload) {
        return await getSpecificGrocerie(payload).then((res) => {
            this.grocerie = res.data.grocerie
            this.persons = res.data.persons
            this.statuses = res.data.statuses
        })
    },

    async createGrocerieAction(payload) {
        const notificationsStore = useNotificationsStore();

        return await createGrocerie(payload).then((res) => {
            if( res.status === 201){
                router.push({name: "grocerieslist"})
                this.resetGrocerieAction()
    
                notificationsStore.setNotification({
                message: res?.data?.detail || "Item created successfully",
                statusCode: res?.status || 201
                })
            }
        })
    },

    async updateGrocerieAction(payload) {
        const notificationsStore = useNotificationsStore();

        return await updateGrocerie(payload).then((res) => {
            console.log(res.data);
        })
    },

    async deleteGrocerieAction(payload) {
        const notificationsStore = useNotificationsStore();

        return await deleteGrocerie(payload).then((res) => {
            if(res.status === 204){
                this.getAllGroceriesAction()
                this.resetGrocerieAction()

                notificationsStore.setNotification({
                    message: res?.data?.detail || "Item deleted successfully",
                    statusCode: res?.status
                })
            }
        })
    }
}