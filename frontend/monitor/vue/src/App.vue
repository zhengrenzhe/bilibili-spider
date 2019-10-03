<template>
    <div>
        <Header/>
        <Stat/>
        <Ctrl/>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from "vue-property-decorator";
    import Header from "./components/Header.vue";
    import Stat from "./components/Stat.vue";
    import Ctrl from "./components/Ctrl.vue";

    @Component({
        components: {
            Header,
            Stat,
            Ctrl,
        },
    })
    export default class App extends Vue {
    }
</script>

<style lang="scss">
    html {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;
    }

    body {
        margin: 0;
        background-color: rgb(252, 251, 254);
    }
</style>
