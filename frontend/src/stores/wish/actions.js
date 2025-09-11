import { getAllWishes, getSpecificWish, createWish, updateWish, deleteWish } from "../../service/wish";
import router from "@/router"


export default {
    async getAllWishesAction() {
        return await getAllWishes().then((res) => {
            this.wishes = res.data.wishes;
            this.tableHeads = res.data.tableHeads;
            this.attributes = res.data.attributes;
        })
    },

    async getSpecificWishAction(payload) {
        return await getSpecificWish(payload).then((res) => {
            console.log(res.data);
        })
    },

    async createWishAction(payload) {
        return await createWish(payload).then((res) => {
            console.log(res.data);
        })
    },

    async updateWishAction(payload) {
        return await updateWish(payload).then((res) => {
            console.log(res.data);
        })
    },

    async deleteWishAction(payload) {
        return await deleteWish(payload).then((res) => {
            console.log(res.data);
        })
    }
}