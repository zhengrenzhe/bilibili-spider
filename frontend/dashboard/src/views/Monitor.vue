<template>
    <div id="monitor">
        <cpu/>
    </div>
</template>

<script>
    import Cpu from "../components/Cpu";

    export default {
        name: "Monitor",
        components: {
            Cpu,
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