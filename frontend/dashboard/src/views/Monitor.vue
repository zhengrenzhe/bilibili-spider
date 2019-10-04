<template>
    <div id="monitor">
        <cpu/>
        <network/>
        <memory/>
    </div>
</template>

<script>
    import Cpu from "../components/Cpu";
    import Network from "../components/Network";
    import Memory from "../components/Memory";

    export default {
        name: "Monitor",
        components: {
            Cpu,
            Network,
            Memory,
        },
    };
</script>

<style scoped lang="scss">
    #monitor {
        padding: 20px;
        display: grid;
        grid-template-columns: repeat(4, 300px);
        grid-auto-flow: row dense;
        grid-gap: 20px;
    }
</style>