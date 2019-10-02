<template>
    <div>
        <Header/>
        <Stat/>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from "vue-property-decorator";
    import Header from "./components/Header.vue";
    import Stat from "./components/Stat.vue";

    @Component({
        components: {
            Header,
            Stat,
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
    }
</style>
