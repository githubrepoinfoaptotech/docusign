import { Box, Typography } from '@mui/material'
import React from 'react'
import AccountCircleIcon from '@mui/icons-material/AccountCircle';

const Dashboard: React.FC = () => {
  return (
    <div>
      <Box sx={{ backgroundColor: "black", color: "white", height: "300px" }} >
        <Box sx={{ p: 4 }} >
          <Box sx={{display:"flex", gap:"20px"}}>
            <AccountCircleIcon sx={{fontSize:"4rem"}} />
            <Typography variant='h3' >
              Welcome
            </Typography>
          </Box>

        </Box>


      </Box>

    </div>
  )
}

export default Dashboard