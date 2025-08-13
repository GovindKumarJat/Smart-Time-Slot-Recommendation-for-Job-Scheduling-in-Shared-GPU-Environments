# app.py

import numpy as np
from datetime import datetime, timedelta

def create_prediction_function(model):
    def predict_turnaround_time_hourly(cpu_milli, memory_mib, num_gpu, gpu_milli):
        qos_level = 2
        pod_phase_Failed = 0
        pod_phase_Running = 0
        pod_phase_Succeeded = 0

        current_datetime = datetime.now()
        current_day_of_week = current_datetime.weekday()
        current_hour = current_datetime.hour

        predicted_turnaround_times = {}

        for hour in range(current_hour, 24):
            job_features_at_hour = np.array([[ 
                cpu_milli,
                memory_mib,
                num_gpu,
                gpu_milli,
                np.log1p(cpu_milli),
                np.log1p(memory_mib),
                np.log1p(gpu_milli),
                (gpu_milli / 1000) * num_gpu,
                qos_level,
                hour,
                current_day_of_week,
                1 if 10 <= hour <= 18 else 0,
                pod_phase_Failed,
                pod_phase_Running,
                pod_phase_Succeeded
            ]])
            transformed = model.predict(job_features_at_hour)
            predicted_turnaround_times[(0, hour)] = np.expm1(transformed)[0]

        tomorrow_datetime = current_datetime + timedelta(days=1)
        tomorrow_day_of_week = tomorrow_datetime.weekday()

        for hour in range(24):
            job_features_at_hour = np.array([[ 
                cpu_milli,
                memory_mib,
                num_gpu,
                gpu_milli,
                np.log1p(cpu_milli),
                np.log1p(memory_mib),
                np.log1p(gpu_milli),
                (gpu_milli / 1000) * num_gpu,
                qos_level,
                hour,
                tomorrow_day_of_week,
                1 if 10 <= hour <= 18 else 0,
                pod_phase_Failed,
                pod_phase_Running,
                pod_phase_Succeeded
            ]])
            transformed = model.predict(job_features_at_hour)
            predicted_turnaround_times[(1, hour)] = np.expm1(transformed)[0]

        best_time_key = min(predicted_turnaround_times, key=predicted_turnaround_times.get)
        best_day_offset, best_hour = best_time_key
        min_predicted_tat = predicted_turnaround_times[best_time_key]

        recommended_datetime = current_datetime.replace(minute=0, second=0, microsecond=0) + timedelta(days=best_day_offset)
        recommended_datetime = recommended_datetime.replace(hour=best_hour)

        output_text = "Predicted Turnaround Times:\n"
        output_text += "Remaining Hours Today:\n"
        for hour in range(current_hour, 24):
            output_text += f"  Hour {hour:02d}: {predicted_turnaround_times[(0, hour)]:.2f} minutes\n"
        output_text += "\nHours Tomorrow:\n"
        for hour in range(24):
            output_text += f"  Hour {hour:02d}: {predicted_turnaround_times[(1, hour)]:.2f} minutes\n"

        day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        output_text += f"\nOverall Recommended Time Slot: {day_names[recommended_datetime.weekday()]} at Hour {best_hour:02d} ({min_predicted_tat:.2f} minutes)"
        output_text += f"\nRecommended Time Slot (Future): {recommended_datetime.strftime('%Y-%m-%d %H:%M:%S')}"

        return output_text

    return predict_turnaround_time_hourly
