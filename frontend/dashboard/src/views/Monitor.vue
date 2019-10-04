<template>
    <div id="monitor">
        <cpu/>
        <network/>
        <memory/>
        <disk/>
    </div>
</template>

<script>
    import Cpu from "../components/Cpu";
    import Network from "../components/Network";
    import Memory from "../components/Memory";
    import Disk from "../components/Disk";

    export default {
        name: "Monitor",
        components: {
            Cpu,
            Network,
            Memory,
            Disk,
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