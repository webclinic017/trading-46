import { Card, CardContent, TextField, Box, Select } from '@mui/material';
import { Task } from '../../types';

type TaskItemProps = {
  task: Task;
};

const TaskItem = ({ task }: TaskItemProps) => {
  return (
    <Card>
      <CardContent>{task.title}</CardContent>
      <Select
        native
        value={task.status}
        inputProps={{
          name: 'status',
          id: 'status',
        }}
      >
        <option value={'todo'}>Todo</option>
        <option value={'in-progress'}>In Progress</option>
        <option value={'done'}>Done</option>
      </Select>
      
    </Card>
  );
};

export default TaskItem;
