import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

import cfg from "../../../services.json";

Vue.use(Vuex);

let host, port;

if (window.env === "prod") {
    host = cfg["dashboard-api-prod"].host;
    port = cfg["dashboard-api-prod"].port;
} else {
    host = cfg["dashboard-api-dev"].host;
    port = cfg["dashboard-api-dev"].port;
}

const API_BASE = `http://${host}:${port}`;

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