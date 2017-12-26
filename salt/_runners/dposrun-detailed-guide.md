dposrun.disable_forging:                                                     
    
        Disable delegate forging based on DPOS system and delegate name
    
        CLI Example:
    
            salt-run dposrun.disable_forging lisk slasheks
        
dposrun.enable_forging:
    
        Enable delegate forging based on DPOS system and delegate name
    
        CLI Example:
    
            salt-run dposrun.enable_forging lisk slasheks
        
dposrun.forging_notify:
    
        Notify via slack if delegate is not forging
    
        CLI Example:
    
            salt-run dposrun.forging_notify lisk slasheks
        
dposrun.is_forging:
    
        Check if a delegate is forging based on DPOS system and delegate name
    
        CLI Example:
    
            salt-run dposrun.is_forging lisk slasheks
        
dposrun.missed_block_notify:
    
        Notify via slack if last block was generated more than 20m ago
    
        CLI Example:
    
            salt-run dposrun.missed_block_notify lisk slasheks
