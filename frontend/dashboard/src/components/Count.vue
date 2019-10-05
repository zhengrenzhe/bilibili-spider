<template>
    <card column="4">
        <card-title>
            Count
            <div class="count">
                Total: {{count}} videos
            </div>
        </card-title>
        <canvas id="count-chart"></canvas>
    </card>
</template>

<script>
    import Card from "./Card";
    import CardTitle from "./CardTitle";
    import Chart from "chart.js";

    const now = Date.now();

    export default {
        name: "Count",
        components: {
            Card,
            CardTitle,
        },
        data() {
            return {
                count: 0,
                counts: [],
            };
        },
        mounted() {
            this.countChart = new Chart(document.getElementById("count-chart").getContext("2d"), {
                type: "bar",
                data: {
                    datasets: [
                        {
                            borderColor: "#e74c3c",
                            data: Array(60).fill(0).map((_, i) => ({
                                y: null,
                                t: new Date(now - (1000 * i)),
                            })),
                            type: "line",
                            pointRadius: 0,
                            fill: false,
                            borderWidth: 2,
                        },
                    ],
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    legend: {
                        display: false,
                    },
                    animation: {
                        duration: 0,
                    },
                    layout: {
                        padding: {
                            top: 2,
                            bottom: 2,
                        },
                    },
                    scales: {
                        xAxes: [{
                            // display: false,
                            type: "time",
                            distribution: "series",
                            ticks: {
                                source: "data",
                                autoSkip: true,
                            },
                        }],
                        yAxes: [{
                            // display: false,
                        }],
                    },
                },
            });

            this.$store.subscribe((_, state) => {
                if (!state.video_count) {
                    return;
                }

                this.countChart.data.datasets[0].data = this.appendTimeSeries({
                    y: state.video_count,
                    t: new Date(),
                });

                this.countChart.update();
            });
        },
        methods: {
            appendTimeSeries(newData) {
                const s = this.countChart.data.datasets[0].data.slice(1);
                s.push(newData);
                return s;
            },
        },
    };
</script>

<style scoped lang="scss">
    .count {
        margin-left: 10px;
        font-size: 20px;
    }
</style>