import { getAllGroceriesStatuses, getSpecificGroceriesStatus, createGroceriesStatus, updateGroceriesStatus, deleteGroceriesStatus } from "../../service/grocerieStatus";
import router from "@/router"


export default {
    async getAllGroceriesStatusesAction() {
        return await getAllGroceriesStatuses().then((res) => {
            console.log(res.data);
        })
    },

    async getSpecificGroceriesStatusAction(payload) {
        return await getSpecificGroceriesStatus(payload).then((res) => {
            console.log(res.data);
        })
    },
    
    async createGroceriesStatusAction(payload) {
        return await createGroceriesStatus(payload).then((res) => {
            console.log(res.data);
        })
    },

    async updateGroceriesStatusAction(payload) {
        return await updateGroceriesStatus(payload).then((res) => {
            console.log(res.data);
        })
    },

    async deleteGroceriesStatusAction(payload) {
        return await deleteGroceriesStatus(payload).then((res) => {
            console.log(res.data);
        })
    }
}