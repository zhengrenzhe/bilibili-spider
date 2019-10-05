<template>
    <card column="4">
        <card-title>
            Processes
            <div class="core" v-if="ctrl">
                PID {{ctrl["supervisor_pid"]}}
                &nbsp;&nbsp;&nbsp;&nbsp;
                State {{ctrl["supervisor_state"]["statename"]}}
            </div>
        </card-title>
        <div class="groups">
            <div class="group" v-for="(g, gName) in groups" :key="gName">
                <div class="group-title">
                    <font-awesome-icon icon="server"/>
                    <div class="content">
                        {{gName}}
                        &nbsp;
                        ({{g.length}} worker{{`${g.length === 1 ? "" : "s"}`}})
                    </div>
                    <button class="group-ctrl"
                            v-if="g.filter(q => q.state !== 20 ).length === g.length"
                            @click="startGroup(gName)"
                    >
                        Start All
                    </button>
                    <button class="group-ctrl"
                            v-if="g.filter(q => q.state === 20 ).length === g.length"
                            @click="stopGroup(gName)"
                    >
                        Stop All
                    </button>
                </div>
                <div class="group-workers">
                    <div v-for="gi in g"
                         :key="gi.name"
                         :class="{
                            'worker': true,
                            'running': gi.state === 20,
                            'stopped': gi.state === 0,
                            'backoff': gi.state === 30,
                            'fatal': gi.state === 200,
                            'unknown': gi.state === 1000,
                            'exited': gi.state === 100
                         }"
                    >
                        <div class="indicate"></div>
                        <div class="meta">
                            <div class="name">{{gi.name}} <span class="state">{{gi["statename"]}}</span></div>
                            <div class="desc">{{gi.description}}</div>
                        </div>
                        <div class="ctrl">
                            <button class="ctrl-btn"
                                    v-if="gi.state === 20"
                                    @click="stopWorker(gName, gi.name)"
                            >
                                Stop
                            </button>
                            <button class="ctrl-btn"
                                    v-if="gi.state !== 20"
                                    @click="startWorker(gName, gi.name)"
                            >
                                Start
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </card>
</template>

<script>
    import axios from "axios";
    import {API_BASE} from "../store";

    import Card from "./Card";
    import CardTitle from "./CardTitle";

    export default {
        name: "Processes",
        components: {
            Card, CardTitle,
        },
        computed: {
            groups() {
                if (!this.$store.state.stat || !this.$store.state.stat.processes) {
                    return [];
                }

                const groups = {};
                const workers = this.$store.state.stat.processes.worker;

                workers.forEach((w) => {
                    groups[w.group] = groups[w.group] || [];
                    groups[w.group].push(w);
                });

                return groups;
            },
            ctrl() {
                const d = this.$store.state.stat;
                if (!d || !d.processes) return null;
                return d.processes["ctrl"];
            },
        },
        methods: {
            stopGroup(groupName) {
                axios.get(`${API_BASE}/stop_process_group/${groupName}`);
            },
            startGroup(groupName) {
                axios.get(`${API_BASE}/start_process_group/${groupName}`);
            },
            stopWorker(groupName, workerName) {
                axios.get(`${API_BASE}/stop_process/${groupName}:${workerName}`);
            },
            startWorker(groupName, workerName) {
                axios.get(`${API_BASE}/start_process/${groupName}:${workerName}`);
            },
        },
    };
</script>

<style scoped lang="scss">
    .core {
        font-size: 18px;
        margin-left: 20px;
        color: #2ecc71;
    }

    .groups {
        display: flex;
        flex-wrap: wrap;

        .group {
            width: 300px;
            margin: 0 10px 20px;
            box-shadow: 0 0 2px 0 #c3c3c3;
            padding: 10px;
            border-radius: 4px;

            .group-title {
                display: flex;
                align-items: center;
                font-size: 18px;

                .content {
                    margin: 0 auto 0 10px;
                }
            }

            .group-workers {
                .worker {
                    display: flex;
                    background-color: #F8FAFC;
                    padding: 4px 8px 6px;
                    border-radius: 4px;
                    margin-top: 10px;

                    &.running {
                        .meta .name .state {
                            color: #2ecc71;
                        }

                        .indicate:before {
                            background-color: #2ecc71;
                        }
                    }

                    &.stopped {
                        .meta .name .state {
                            color: #bdc3c7;
                        }

                        .indicate:before {
                            background-color: #bdc3c7;
                        }
                    }

                    &.backoff, &.fatal, &.unknown, &.exited {
                        .meta .name .state {
                            color: #e74c3c;
                        }

                        .indicate:before {
                            background-color: #e74c3c;
                        }
                    }

                    .indicate {
                        &:before {
                            content: "";
                            width: 8px;
                            height: 8px;
                            border-radius: 100%;
                            display: block;
                            margin-top: 6px;
                        }
                    }

                    .meta {
                        margin-left: 8px;
                        flex: 1;

                        .name {
                            font-size: 16px;

                            .state {
                                font-size: 14px;
                                margin-left: 4px;
                                text-transform: lowercase;
                            }
                        }

                        .desc {
                            margin-top: 4px;
                            font-size: 14px;
                            color: #808e9b;
                        }
                    }

                    .ctrl {
                        display: flex;
                        align-items: center;

                        .ctrl-btn {
                        }
                    }
                }
            }
        }
    }
</style>