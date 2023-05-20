import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';

function Dashboard({ user }) {
  const [groups, setGroups] = useState([]);
  const [newGroupName, setNewGroupName] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    fetchGroups();
  }, []);

  const fetchGroups = async () => {
    try {
      const response = await axios.get('/api/groups');
      setGroups(response.data.groups);
    } catch (error) {
      console.error('Error fetching groups:', error);
    }
  };

  const handleAddGroup = async () => {
    try {
      const response = await axios.post('/api/group/create', {
        user_id: user.user_id,
        group_name: newGroupName,
      });
      if (response.data.group_id) {
        navigate(`/generator/${response.data.group_id}`);
      }
    } catch (error) {
      console.error('Error creating group:', error);
    }
  };

  return (
    <div className="dashboard">
      <h2>My Groups</h2>
      <table>
        <thead>
          <tr>
            <th>Group Name</th>
            <th>Members</th>
            <th>Winning Idea</th>
          </tr>
        </thead>
        <tbody>
          {groups.map((group) => (
            <tr key={group.id}>
              <td>
                <Link to={`/group/${group.id}`}>{group.name}</Link>
              </td>
              <td>{group.members.join(', ')}</td>
              <td>{group.winningIdea}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div className="add-group">
        <input
          type="text"
          placeholder="New Group Name"
          value={newGroupName}
          onChange={(e) => setNewGroupName(e.target.value)}
        />
        <button onClick={handleAddGroup}>Add Group</button>
      </div>
    </div>
  );
}

export default Dashboard;
