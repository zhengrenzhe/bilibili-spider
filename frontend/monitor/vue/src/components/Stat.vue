<template>
    <div class="stat">
    </div>
</template>

<script>
    export default {
        name: "Stat",
        computed: {
            processes() {
                const d = this.$store.state.stat.data;
                return d ? d.processes : null;
            },
            system() {
                const d = this.$store.state.stat.data;
                return d ? d.system : null;
            },
        },
    }
    ;
</script>

<style scoped lang="scss">

</style>