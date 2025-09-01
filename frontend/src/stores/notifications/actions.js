export default {
    setNotification(payload){
        this.message = payload.message
        this.statusCode = payload.statusCode
    },
    clearNotifications(){
        this.statusCode = null
        this.message = null
    }
}