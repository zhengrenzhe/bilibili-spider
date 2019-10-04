<template>
    <div id="nav">
        <router-link to="/" class="logo" title="bilibili dashboard">
            <font-awesome-icon icon="robot" size="2x"/>
        </router-link>

        <router-link to="/" class="link" title="monitor">
            <font-awesome-icon icon="chart-bar" size="lg"/>
        </router-link>

        <router-link to="/log" class="link" title="log">
            <font-awesome-icon icon="bolt" size="lg"/>
        </router-link>
    </div>
</template>

<script>
    export default {
        name: "Nav",
    };
</script>

<style scoped lang="scss">
    #nav {
        display: flex;
        flex-direction: column;
        align-items: center;
        height: 100%;
        background-color: #0052CC;
        color: #fff;
        padding: 14px 0;
    }

    .logo {
        margin-bottom: 40px;
    }

    .link {
        margin-bottom: 30px;
    }

    a {
        color: #fff;
        text-decoration: none;
    }
</style>