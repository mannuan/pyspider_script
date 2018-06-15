function regex(str) {
    if(/^::\/128$|^([0]{4}:){7}[0]{4}$/.test(str)){
        return 'Unspecified'
    }else if(/^::1\/128$|^([0]{4}:){7}[0]{3}1$/.test(str)){
        return 'Loopback'
    }else if(/^FE80::\/10$|^FE[89AB]{1}[0-9A-F]{1}(:[0-9A-F]{4}){6}:[0-9A-F]{4}$/.test(str)){
        return 'LinkLocal'
    }else if(/^FEC0::\/10$|^FE[CDEF]{1}[0-9A-F]{1}(:[0-9A-F]{4}){6}:[0-9A-F]{4}$/.test(str)){
        return 'SiteLocal'
    }else if(/^FF00::\/10$|^FF[0-9A-F]{2}(:[0-9A-F]{4}){6}:[0-9A-F]{4}$/.test(str)){
        return 'MultiUnicast'
    }else if(/^([0-9A-F]{4}:){7}[0-9A-F]{4}$/.test(str)){
        return 'Globalcast'
    }
    else{
        return 'Error'
    }
}