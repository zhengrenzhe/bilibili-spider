import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import {library} from "@fortawesome/fontawesome-svg-core";
import {
    faBolt,
    faCertificate,
    faChartBar,
    faLongArrowAltDown,
    faLongArrowAltUp,
    faRobot,
    faServer,
    faUserSecret,
} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";

library.add(faUserSecret, faCertificate, faRobot, faChartBar, faBolt, faLongArrowAltUp, faLongArrowAltDown, faServer);

Vue.component("font-awesome-icon", FontAwesomeIcon);

Vue.config.productionTip = false;

new Vue({
    router,
    store,
    render: h => h(App),
}).$mount("#app");
