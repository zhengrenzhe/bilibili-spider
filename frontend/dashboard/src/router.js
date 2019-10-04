import Vue from "vue";
import Router from "vue-router";

import Monitor from "./views/Monitor.vue";
import Log from "./views/Log.vue";

Vue.use(Router);

export default new Router({
    mode: "history",
    base: process.env.BASE_URL,
    routes: [
        {
            path: "/",
            name: "monitor",
            component: Monitor,
        },
        {
            path: "/log",
            name: "log",
            component: Log,
        },
    ],
});
