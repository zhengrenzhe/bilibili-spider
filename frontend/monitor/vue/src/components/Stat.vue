<template>
    <div class="stat">
        <div class="block cpu">
            <canvas id="cpu" width="240px" height="240px"></canvas>
        </div>
        <div class="block memory">
            <canvas id="memory" width="240px" height="240px"></canvas>
        </div>
        <div class="block network">
            <canvas id="network" width="240px" height="240px"></canvas>
        </div>
        <div class="block disk">
            <canvas id="disk" width="240px" height="240px"></canvas>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Stat",
        computed: {
            processes() {
                const d = this.$store.state.stat;
                return d ? d.processes : null;
            },
            system() {
                const d = this.$store.state.stat;
                return d ? d.system : null;
            },
        },
        created() {
            this.$store.subscribe((_, state) => {
            });
        },
        methods: {},
    }
    ;
</script>

<style scoped lang="scss">
    .stat {
        display: flex;
        flex-shrink: 0;
        flex-wrap: wrap;
        justify-content: space-evenly;
        margin: 40px 0;
        align-items: center;
    }

    .block {
        width: 240px;
        height: 240px;
        background-color: #fff;
        box-shadow: 0 0 2px 0 rgb(195, 195, 195);
        border-radius: 4px;
        margin-bottom: 20px;

        canvas {
            width: 100%;
            height: 100%;
        }
    }
</style>