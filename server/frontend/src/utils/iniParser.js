export function parse(text) {
    const result = {
        reticulum: {},
        logging: {},
        interfaces: [],
        _unknown: {},
    };
    let currentSection = null;
    let currentInterface = null;
    for (const raw of text.split("\n")) {
        const line = raw.trimEnd();
        // Double-bracket interface section: [[Name]]
        const ifaceMatch = line.match(/^\s*\[\[(.+?)\]\]/);
        if (ifaceMatch) {
            if (currentInterface)
                result.interfaces.push(currentInterface);
            currentInterface = { name: ifaceMatch[1].trim(), fields: {} };
            currentSection = null;
            continue;
        }
        // Single-bracket global section: [name]
        const sectionMatch = line.match(/^\s*\[([^\[\]]+)\]/);
        if (sectionMatch) {
            if (currentInterface) {
                result.interfaces.push(currentInterface);
                currentInterface = null;
            }
            currentSection = sectionMatch[1].trim().toLowerCase();
            if (currentSection !== "reticulum" && currentSection !== "logging") {
                result._unknown[currentSection] = result._unknown[currentSection] ?? {};
            }
            continue;
        }
        // Key = value
        const kvMatch = line.match(/^[ \t]+([^=]+?)\s*=\s*(.*)/);
        if (!kvMatch)
            continue;
        const key = kvMatch[1].trim();
        const value = kvMatch[2].trim();
        if (currentInterface) {
            currentInterface.fields[key] = value;
        }
        else if (currentSection === "reticulum") {
            result.reticulum[key] = value;
        }
        else if (currentSection === "logging") {
            result.logging[key] = value;
        }
        else if (currentSection && result._unknown[currentSection]) {
            result._unknown[currentSection][key] = value;
        }
    }
    if (currentInterface)
        result.interfaces.push(currentInterface);
    return result;
}
export function serialize(config) {
    const lines = [];
    const writeSection = (name, fields) => {
        lines.push(`[${name}]`);
        for (const [k, v] of Object.entries(fields)) {
            lines.push(`  ${k} = ${v}`);
        }
        lines.push("");
    };
    if (Object.keys(config.reticulum).length)
        writeSection("reticulum", config.reticulum);
    if (Object.keys(config.logging).length)
        writeSection("logging", config.logging);
    for (const [name, fields] of Object.entries(config._unknown)) {
        writeSection(name, fields);
    }
    for (const iface of config.interfaces) {
        lines.push(`[[${iface.name}]]`);
        for (const [k, v] of Object.entries(iface.fields)) {
            lines.push(`  ${k} = ${v}`);
        }
        lines.push("");
    }
    return lines.join("\n");
}
export function getBool(value) {
    return /^(yes|true|1)$/i.test(value ?? "");
}
export function setBool(value) {
    return value ? "yes" : "no";
}
