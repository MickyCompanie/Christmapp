import { getAllGroceriesStatuses, getEmptyGroceriesStatus, getSpecificGroceriesStatus, createGroceriesStatus, updateGroceriesStatus, deleteGroceriesStatus } from "../../service/grocerieStatus";
import { useNotificationsStore } from "@/stores/notifications";
import router from "@/router"

export default {
    async getAllGroceriesStatusesAction() {
        return await getAllGroceriesStatuses().then((res) => {
            this.groceriesStatuses = res.data.groceriesStatuses;
            this.tableHeads = res.data.tableHeads;
            this.attributes = res.data.attributes;
        }).catch((error) => {
            console.error("Error fetching groceries statuses:", error); 
        })
    },

    async resetGroceriesStatusAction() {
        this.groceriesStatus = null;
    },

    async getEmptyGroceriesStatusAction() {
        return await getEmptyGroceriesStatus().then((res) => {
            this.groceriesStatus = res.data;
        })
    },

    async getSpecificGroceriesStatusAction(payload) {
        const notificationsStore = useNotificationsStore();

        return await getSpecificGroceriesStatus(payload).then((res) => {
            this.groceriesStatus = res.data;
        }).catch((error) => {
            notificationsStore.setNotification({
                message: error?.response?.data?.detail || "something went wrong",
                statusCode: error?.response?.status || 500
            });
        })
    },
    
    async createGroceriesStatusAction(payload) {
        const notificationsStore = useNotificationsStore();

        return await createGroceriesStatus(payload).then((res) => {
            router.push({name: "groceriesStatusList"})

            notificationsStore.setNotification({
            message: res?.data?.detail || "Status created successfully",
            statusCode: res?.status || 201
            })
        }).catch((error) => {
            notificationsStore.setNotification({
                message: error?.response?.data?.detail || null,
                statusCode: error?.response?.status || 500
            });
        })
    },

    async updateGroceriesStatusAction(payload) {
        const notificationsStore = useNotificationsStore();

        return await updateGroceriesStatus(payload).then((res) => {
            router.push({name: "groceriesStatusList"})

            notificationsStore.setNotification({
            message: res?.data?.detail || "Status updated successfully",
            statusCode: res?.status || 201
            })
        }).catch((error) => {
            notificationsStore.setNotification({
                message: error?.response?.data?.detail || null,
                statusCode: error?.response?.status || 500
            });
        })
    },

    async deleteGroceriesStatusAction(payload) {
        const notificationsStore = useNotificationsStore();

        return await deleteGroceriesStatus(payload).then((res) => {
            this.getAllGroceriesStatusesAction()

            notificationsStore.setNotification({
            message: res?.data?.detail || "Status deleted successfully",
            statusCode: res?.status || 201
            })
        }).catch((error) => {
             notificationsStore.setNotification({
                message: error?.response?.data?.detail || null,
                statusCode: error?.response?.status || 500
            });
        })
    }
}