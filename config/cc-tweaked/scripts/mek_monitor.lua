-- MekPack Sci-Fi Terminal: Mekanism Reactor & Energy Monitor
-- Displays live telemetry for Fission/Fusion Reactors and Energy Storage

local function clear()
    term.clear()
    term.setCursorPos(1, 1)
end

local function drawHeader(title)
    term.setTextColor(colors.cyan)
    print("========================================")
    print("   MEKPACK // " .. title)
    print("========================================")
    term.setTextColor(colors.white)
end

local function findPeripheral(typeKeyword)
    local names = peripheral.getNames()
    for _, name in ipairs(names) do
        local pType = peripheral.getType(name) or ""
        if string.find(string.lower(pType), string.lower(typeKeyword)) or string.find(string.lower(name), string.lower(typeKeyword)) then
            return peripheral.wrap(name), name
        end
    end
    return nil, nil
end

local function main()
    while true do
        clear()
        drawHeader("CORE TELEMETRY MONITOR")
        
        local reactor, rName = findPeripheral("reactor")
        local energy, eName = findPeripheral("energy")

        if reactor then
            term.setTextColor(colors.yellow)
            print("[REACTOR CONNECTED: " .. rName .. "]")
            term.setTextColor(colors.white)
            
            pcall(function()
                if reactor.getStatus then
                    local status = reactor.getStatus() and "ACTIVE" or "SCRAM / OFFLINE"
                    print("Status:      " .. status)
                end
                if reactor.getTemperature then
                    local temp = math.floor(reactor.getTemperature())
                    print("Temperature: " .. temp .. " K")
                end
                if reactor.getDamagePercent then
                    local dmg = reactor.getDamagePercent()
                    print("Core Damage: " .. dmg .. " %")
                end
            end)
        else
            term.setTextColor(colors.gray)
            print("[REACTOR] Scanning for connected peripheral...")
        end

        print("")
        if energy then
            term.setTextColor(colors.lime)
            print("[ENERGY MATRIX: " .. eName .. "]")
            term.setTextColor(colors.white)
            pcall(function()
                if energy.getEnergy and energy.getMaxEnergy then
                    local cur = energy.getEnergy()
                    local maxE = energy.getMaxEnergy()
                    local pct = math.floor((cur / maxE) * 100)
                    print("Capacity: " .. pct .. "% (" .. math.floor(cur) .. " / " .. math.floor(maxE) .. " FE)")
                end
            end)
        else
            term.setTextColor(colors.gray)
            print("[ENERGY] Scanning for energy storage peripheral...")
        end

        term.setTextColor(colors.lightGray)
        print("\nRefreshing telemetry every 2s. Press Ctrl+T to exit.")
        sleep(2)
    end
end

main()
