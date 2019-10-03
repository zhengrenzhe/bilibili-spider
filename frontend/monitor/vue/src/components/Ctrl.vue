<template>
    <div class="ctrl">
        <div class="title" v-if="processes">
            Supervisor
            <span class="title-meta">
                PID: {{processes.ctrl["supervisor_pid"]}}
                &nbsp;&nbsp;&nbsp;&nbsp;
                STATE: {{processes.ctrl["supervisor_state"]["statename"]}}
            </span>
        </div>

        <div class="groups">
            <div class="group" v-for="(g, gName) in groups">
                <div class="group-title">
                    <div class="group-name">
                        {{gName}} - ({{g.length}})
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
                         :class="{
                            'group-worker-item': true,
                            'running': gi.state === 20,
                            'stopped': gi.state === 0,
                            'backoff': gi.state === 30,
                            'fatal': gi.state === 200,
                            'unknown': gi.state === 1000,
                            'exited': gi.state === 100
                         }"
                    >
                        <div class="group-worker-meta">
                            <span class="group-worker-name">{{gi.name}}</span>
                            <span class="group-worker-state">{{gi["statename"]}}</span>
                            <button class="group-worker-ctrl"
                                    v-if="gi.state === 20"
                                    @click="stopWorker(gName, gi.name)"
                            >
                                Stop
                            </button>
                            <button class="group-worker-ctrl"
                                    v-if="gi.state !== 20"
                                    @click="startWorker(gName, gi.name)"
                            >
                                Start
                            </button>
                        </div>
                        <div class="group-worker-detail">
                            {{gi.description}}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {API_BASE} from "@/store";
    import axios from "axios";

    export default {
        name: "Ctrl",
        computed: {
            processes() {
                const d = this.$store.state.stat;
                return d ? d.processes : null;
            },
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
    .ctrl {
        margin: 40px 20px;
        box-shadow: 0 0 2px 0 #c3c3c3;
        background-color: #fff;
        border-radius: 4px;
        padding: 10px 16px;
    }

    .title {
        font-size: 26px;
        font-weight: 600;
        color: #33373b;
    }

    .title-meta {
        font-size: 16px;
        color: #2ecc71;
        margin-left: 20px;
    }

    .groups {
        display: flex;
        flex-wrap: wrap;
        flex-direction: row;

        .group {
            border: 1px solid #bdc3c7;
            border-radius: 4px;
            margin: 10px;
            min-width: 260px;
            padding: 4px 10px 8px;

            .group-title {
                display: flex;
                align-items: center;
                font-weight: 600;

                .group-name {
                    padding: 4px 0;
                    font-size: 18px;
                }

                .group-ctrl {
                    font-size: 12px;
                    border-radius: 4px;
                    outline: none;
                    cursor: pointer;
                    margin-left: auto;
                }
            }

            .group-workers {
                .group-worker-item {
                    padding: 6px;
                    border: 1px dashed #e0e0e0;
                    border-radius: 4px;
                    margin-top: 8px;

                    &.running {
                        color: #2ecc71;
                    }

                    &.stopped {
                        color: #bdc3c7;
                    }

                    &.backoff, &.fatal, &.unknown, &.exited {
                        color: #e74c3c;
                    }

                    .group-worker-meta {
                        display: flex;
                        align-items: center;
                        user-select: none;

                        .group-worker-ctrl {
                            font-size: 12px;
                            border-radius: 4px;
                            outline: none;
                            cursor: pointer;
                            margin-left: auto;
                        }

                        .group-worker-state {
                            margin-left: 10px;
                            font-size: 12px;
                        }
                    }

                    .group-worker-detail {
                        margin-top: 2px;
                        font-size: 12px;
                    }
                }
            }
        }
    }
</style>