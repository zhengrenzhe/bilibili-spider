<template>
    <card column="1">
        <card-title>
            CPU
            <span class="total_percent" v-if="system">
                {{system["cpu"]["core_count"]}} cores
                -
                {{system["cpu"]["total_percent"]}}%
            </span>
        </card-title>
        <square>
            <canvas id="cpu-chart-root" width="180" height="180"></canvas>
        </square>
    </card>
</template>

<script>
    import Chart from "chart.js";
    import Card from "./Card.vue";
    import CardTitle from "./CardTitle";
    import Square from "./Square";

    export default {
        name: "Cpu",
        components: {
            Card,
            CardTitle,
            Square,
        },
        computed: {
            system() {
                const d = this.$store.state.stat;
                return d ? d.system : null;
            },
        },
        data() {
            return {
                cpuChart: {},
            };
        },
        mounted() {
            this.cpuChart = new Chart(document.getElementById("cpu-chart-root").getContext("2d"), {
                type: "bar",
                data: {
                    labels: [],
                    datasets: [{
                        data: [],
                        backgroundColor: "rgba(255, 99, 132, 0.2)",
                        borderColor: "rgba(255, 99, 132, 1)",
                        borderWidth: 0.5,
                    }],
                },
                options: {
                    legend: {
                        display: false,
                    },
                    scales: {
                        xAxes: [{
                            display: false,
                            barPercentage: 1,
                            categoryPercentage: 0.95,
                        }],
                        yAxes: [{
                            display: false,
                            ticks: {
                                max: 100,
                            },
                        }],
                    },
                },
            });
        },
        created() {
            this.$store.subscribe((_, state) => {
                if (!state.stat.system) {
                    return;
                }

                const p = state.stat.system["cpu"]["percent"];
                this.cpuChart.data.labels = p.map((_, i) => `CPU ${i + 1}`);
                this.cpuChart.data.datasets[0].data = state.stat.system["cpu"]["percent"];
                this.cpuChart.update();
            });
        },
    };
</script>

<style scoped lang="scss">
    .total_percent {
        margin-left: 10px;
        font-size: 20px;
    }

    #cpu-chart-root {
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
    }
</style>