export default {
    getStatusCode: (state) => state.statusCode,
    getMessage: (state) => state.message,
    showNotification: (state) => Boolean(state.message)
}