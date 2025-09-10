import { getAllGroceries, getSpecificGrocerie, createGrocerie, updateGrocerie, deleteGrocerie } from "../../service/grocerie";
import router from "@/router"


export default {
    async getAllGroceriesAction() {
        return await getAllGroceries().then((res) => {
            console.log(res.data);
        })
    },
    async getSpecificGrocerieAction(payload) {
        return await getSpecificGrocerie(payload).then((res) => {
            console.log(res.data);
        })
    },
    async createGrocerieAction(payload) {
        return await createGrocerie(payload).then((res) => {
            console.log(res.data);
        })
    },

    async updateGrocerieAction(payload) {
        return await updateGrocerie(payload).then((res) => {
            console.log(res.data);
        })
    },

    async deleteGrocerieAction(payload) {
        return await deleteGrocerie(payload).then((res) => {
            console.log(res.data);
        })
    }
}