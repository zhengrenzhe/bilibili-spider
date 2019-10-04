<template>
    <div id="monitor">
        <count/>
        <cpu/>
        <network/>
        <memory/>
        <disk/>
        <processes/>
    </div>
</template>

<script>
    import Cpu from "../components/Cpu";
    import Network from "../components/Network";
    import Memory from "../components/Memory";
    import Disk from "../components/Disk";
    import Processes from "../components/Processes";
    import Count from "../components/Count";

    export default {
        name: "Monitor",
        components: {
            Cpu,
            Network,
            Memory,
            Disk,
            Processes,
            Count,
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