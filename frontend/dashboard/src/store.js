import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

const API_BASE = "http://localhost:3000";

const Store = new Vuex.Store({
    state: {
        stat: {},
        video_count: 0,
    },
    mutations: {
        update_stat(state, newStat) {
            state.stat = {...newStat};
        },
        update_video_count(state, newCount) {
            state.video_count = newCount;
        },
    },
});


setInterval(async () => {
    const res = await axios.get(`${API_BASE}/stat_info`);
    Store.commit("update_stat", res.data);
}, 1000);

setInterval(async () => {
    const res = await axios.get(`${API_BASE}/videos_count`);
    Store.commit("update_video_count", res.data.count);
}, 1000);

export default Store;
export {API_BASE};