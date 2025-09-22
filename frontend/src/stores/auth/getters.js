export default {
    isAuthenticated: (state) => !!state.accessToken,
    getUser: (state) => state.user,
    getAccessToken: (state) => state.accessToken,
    getRefreshToken: (state) => state.refreshToken,
    getPersonUid: (state) => state.user?.person?.uid,
    getUsers: (state) => state.users
};