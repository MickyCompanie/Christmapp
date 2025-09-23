import { getAllPerson, getEmptyPerson, getSpecificPerson, createPerson, updatePerson, deletePerson } from "../../service/person";
import { useNotificationsStore } from "@/stores/notifications";
import router from "@/router"


export default {

    async getAllPersonAction(){
        return await getAllPerson()
        .then((response) => {
            this.persons = response.data.persons
            this.tableHeads = response.data.tableHeads;
            this.attributes = response.data.attributes;
        })
    },

    async resetPersonAction(){
        this.person = null
    },

    async getEmptyPersonAction(){
        return await getEmptyPerson()
        .then((response) => {
            this.person = response.data
        }).catch((error) => {

        })
    },

    async getSpecificPersonAction(payload){
        return await getSpecificPerson(payload)
        .then((response) => {
            this.person = response.data
        })
    },

    async createPersonAction(payload){
        const notificationsStore = useNotificationsStore();

        return await createPerson(payload)
        .then((response) => {
            router.push({name: 'personlist'})
            this.resetPersonAction()

            notificationsStore.setNotification({
            message: res?.data?.detail || "Person created successfully",
            statusCode: res?.status || 201
            })

        }).catch((error) => {
            notificationsStore.setNotification({
                message: error?.response?.data?.detail || null,
                statusCode: error?.response?.status || 500
            });
        })
    },
    
    async updatePersonAction(payload){
        const notificationsStore = useNotificationsStore();

        return await updatePerson(payload).then((res) => {
            router.push({name: "personlist"})
            this.resetPersonAction()

            notificationsStore.setNotification({
            message: res?.data?.detail || "Person updated successfully",
            statusCode: res?.status || 201
            })

        }).catch((error) => {
            notificationsStore.setNotification({
                message: error?.response?.data?.detail || null,
                statusCode: error?.response?.status || 500
            });
        })
    },

    async deletePersonAction(payload){
        const notificationsStore = useNotificationsStore();
        
        return await deletePerson(payload)
        .then((response) => {
            this.getAllPersonAction()

            notificationsStore.setNotification({
            message: res?.data?.detail || "Person deleted successfully",
            statusCode: res?.status || 201
            })

        }).catch((error) => {
            notificationsStore.setNotification({
                message: error?.response?.data?.detail || null,
                statusCode: error?.response?.status || 500
            });
        })
    },
};