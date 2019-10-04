<template>
    <div id="app">
        <div id="nav-container">
            <Nav/>
        </div>
        <div id="router-view">
            <router-view/>
        </div>
    </div>
</template>

<script>
    import Nav from "./views/Nav.vue";

    export default {
        name: "Index",
        components: {
            Nav,
        },
    };
</script>

<style lang="scss">
    html, body, #app {
        height: 100%;
    }

    body {
        font-family: 'Source Sans Pro', sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        margin: 0;
        background-color: rgb(244, 245, 247);
        line-height: 1;
    }

    #app {
        display: flex;
    }

    #nav-container {
        width: 60px;
    }

    #router-view {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        flex: 1;
        overflow: auto;
    }
</style>
