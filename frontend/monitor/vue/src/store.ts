import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

const API_BASE = "http://localhost:3000";

const Store = new Vuex.Store({
    state: {
        stat: {},
        videos_count: 0,
    },
    mutations: {
        update_stat(state, newStat) {
            state.stat = { ...newStat };
        },
        update_videos_count(state, newCount) {
            state.videos_count = newCount;
        },
    },
});

setInterval(() => {
    axios.get(`${ API_BASE }/stat_info`).then((res) => {
        Store.commit("update_stat", res.data);
    });
}, 1000);

setInterval(() => {
    axios.get(`${ API_BASE }/videos_count`).then((res) => {
        Store.commit("update_videos_count", res.data.count);
    });
}, 1000);


export default Store;
export { API_BASE };
