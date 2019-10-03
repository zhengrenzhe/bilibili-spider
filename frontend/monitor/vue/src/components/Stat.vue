<template>
    <div class="stat">
        <div class="block cpu">
            <div class="block-title">
                CPU {{system && system["cpu"]["total_percent"]}}%
            </div>
            <canvas id="cpu" width="240px" height="180px"></canvas>
        </div>
        <div class="block network">
            <div class="block-title">
                Network
                <div class="network-speed">
                    <div class="up">⬆️ {{system && system["network"]["upload"]}} KB/s</div>
                    <div class="down">⬇️ {{system && system["network"]["download"]}} KB/s</div>
                </div>
            </div>
            <canvas id="network" width="240px" height="180px"></canvas>
        </div>
        <div class="block memory">
            <div class="block-title">
                Memory
            </div>
            <canvas id="memory" width="240px" height="180px">
            </canvas>
        </div>
        <div class="block disk">
            <canvas id="disk" width="240px" height="240px"></canvas>
        </div>
    </div>
</template>

<script>
    import Chart from "chart.js";

    const now = Date.now();

    const uploadTimeSeries = Array(60).fill(0).map((_, i) => ({
        y: null,
        t: new Date(now - (1000 * i)),
    }));

    const downloadTimeSeries = Array(60).fill(0).map((_, i) => ({
        y: null,
        t: new Date(now - (1000 * i)),
    }));

    function appendTimeSeries(arr, item) {
        const n = arr.slice(1);
        n.push(item);
        return n;
    }

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
        data() {
            return {
                cpuChart: {},
                networkChart: {},
                memoryChart: {},
            };
        },
        mounted() {
            this.cpuChart = new Chart(document.getElementById("cpu").getContext("2d"), {
                type: "bar",
                data: {
                    labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                    datasets: [{
                        data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        backgroundColor: "rgba(255, 99, 132, 0.2)",
                        borderColor: "rgba(255, 99, 132, 1)",
                        borderWidth: 0.5,
                    }],
                },
                options: {
                    legend: {
                        display: false,
                    },
                    title: {
                        display: false,
                    },
                    tooltips: {
                        enabled: false,
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

            this.networkChart = new Chart(document.getElementById("network").getContext("2d"), {
                type: "bar",
                data: {
                    datasets: [
                        {
                            borderColor: "#e74c3c",
                            data: uploadTimeSeries,
                            type: "line",
                            pointRadius: 0,
                            fill: false,
                            borderWidth: 2,
                        },
                        {
                            borderColor: "#3498db",
                            data: downloadTimeSeries,
                            type: "line",
                            pointRadius: 0,
                            fill: false,
                            borderWidth: 2,
                        },
                    ],
                },
                options: {
                    legend: {
                        display: false,
                    },
                    title: {
                        display: false,
                    },
                    tooltips: {
                        enabled: false,
                    },
                    animation: {
                        duration: 0,
                    },
                    layout: {
                        padding: {
                            bottom: 2,
                        },
                    },
                    scales: {
                        xAxes: [{
                            display: false,
                            type: "time",
                            distribution: "series",
                            offset: true,
                            ticks: {
                                source: "data",
                                autoSkip: true,
                            },
                        }],
                        yAxes: [{
                            display: false,
                        }],
                    },
                },
            });

            this.memoryChart = new Chart(document.getElementById("memory").getContext("2d"), {
                type: "horizontalBar",
                data: {
                    labels: ["phy", "swap"],
                    datasets: [
                        {
                            label: "used",
                            data: [0, 0],
                            backgroundColor: "#3498db",
                        },
                        {
                            label: "total",
                            data: [0, 0],
                            backgroundColor: "#e2e2e2",
                        },
                    ],
                },

                options: {
                    legend: {
                        display: false,
                    },
                    title: {
                        display: false,
                    },
                    tooltips: {
                        enabled: false,
                    },
                    layout: {
                        padding: {
                            left: 10,
                        },
                    },
                    animation: {
                        duration: 0,
                    },
                    scales: {
                        xAxes: [{
                            stacked: true,
                            display: false,
                        }],
                        yAxes: [{
                            stacked: true,
                            // display: false,
                            barPercentage: 0.4,
                            categoryPercentage: 1,
                        }],
                    },
                },
            });
        },
        created() {
            this.$store.subscribe((_, state) => {
                this.cpuChart.data.datasets[0].data = state.stat.system["cpu"]["percent"];
                this.networkChart.data.datasets[0].data = appendTimeSeries(this.networkChart.data.datasets[0].data, {
                    y: state.stat.system["network"]["upload"],
                    t: new Date(),
                });
                this.networkChart.data.datasets[1].data = appendTimeSeries(this.networkChart.data.datasets[1].data, {
                    y: state.stat.system["network"]["download"],
                    t: new Date(),
                });
                const phyTotal = state.stat.system["memory"]["total"] / Math.pow(1024, 3);
                const swapTotal = state.stat.system["swap"]["total"] / Math.pow(1024, 3);
                this.memoryChart.data.labels = [`Phy(${phyTotal}GB)`, `Swap(${swapTotal}GB)`];
                this.memoryChart.data.datasets[0].data = [
                    state.stat.system["memory"]["used"] / Math.pow(1024, 3),
                    state.stat.system["swap"]["used"] / Math.pow(1024, 3),
                ];
                this.memoryChart.data.datasets[1].data = [
                    phyTotal,
                    swapTotal,
                ];

                this.cpuChart.update();
                this.networkChart.update();
                this.memoryChart.update();
            });
        },
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
        display: flex;
        flex-direction: column;
        width: 240px;
        height: 240px;
        background-color: #fff;
        box-shadow: 0 0 2px 0 rgb(195, 195, 195);
        border-radius: 4px;
        margin-bottom: 20px;

        .block-title {
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            position: relative;
            color: #33373B;
            padding: 0 0 0 15px;

            &:after {
                content: "";
                position: absolute;
                width: 120px;
                height: 1px;
                background: rgb(195, 195, 195);
                bottom: 0;
                left: 0;
                right: 0;
                margin: auto;
            }
        }

        canvas {
            width: 100%;
            height: 100%;
            border-radius: 4px;
        }

        .network-speed, .memory-usage {
            font-size: 14px;
            width: 100px;
            margin-left: 10px;
            flex: 1;

            .up, .phy {
                color: #e74c3c;
            }

            .down, .swap {
                color: #3498db;
            }
        }
    }
</style>