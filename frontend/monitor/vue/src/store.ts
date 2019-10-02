import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

const API_BASE = "http://localhost:3000";

const Store = new Vuex.Store({
    state: {
        stat: {},
        stats: [],
    },
    mutations: {
        update_stat(state, newStat) {
            // @ts-ignore
            state.stats.push(JSON.parse(JSON.stringify(state.stat)));
            state.stat = { ...newStat };
        },
    },
});

setInterval(() => {
    axios.get(`${ API_BASE }/stat_info`).then((res) => {
        Store.commit("update_stat", res.data);
    });
}, 1000);


export default Store;