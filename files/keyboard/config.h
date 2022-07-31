#pragma once

#include "config_common.h"

/* USB Device descriptor parameter */
#define VENDOR_ID 0x594D  // "YM"
#define PRODUCT_ID 0x4975 // "WINGHS"
#define DEVICE_VER 0x0001
#define MANUFACTURER YMDK
#define PRODUCT WINGS HOTSWAP

/* key matrix size */
#define MATRIX_ROWS 5
#define MATRIX_COLS 15

/*
 * Keyboard Matrix Assignments
 *
 * Change this to how you wired your keyboard
 * COLS: AVR pins used for columns, left to right
 * ROWS: AVR pins used for rows, top to bottom
 * DIODE_DIRECTION: COL2ROW = COL = Anode (+), ROW = Cathode (-, marked on diode)
 *                  ROW2COL = ROW = Anode (+), COL = Cathode (-, marked on diode)
 *
 */
#define MATRIX_ROW_PINS { B0, B1, B2, B3, B7 }
#define MATRIX_COL_PINS { D0, D1, D2, D3, D5, D4, D6, D7, B4, F7, F6, F5, F4, F1, F0 }
#define UNUSED_PINS

/* COL2ROW, ROW2COL*/
#define DIODE_DIRECTION ROW2COL

#define QMK_KEYS_PER_SCAN 43

#define FORCE_NKRO

// 1000hz polling rate
#define USB_POLLING_INTERVAL_MS 1

// Chord splitting fix
// https://github.com/qmk/qmk_firmware/pull/10955
#define DEFER_KEYBOARD_REPORT_ENABLE

// Lighting

#define BACKLIGHT_PIN B6
#define BACKLIGHT_LEVELS 5

#define LED_CAPS_LOCK_PIN C7
#define LED_PIN_ON_STATE 0

#define RGB_DI_PIN E2
#ifdef RGB_DI_PIN

    #define RGBLED_NUM 80
    #define RGBLIGHT_EFFECT_BREATHING
    #define RGBLIGHT_EFFECT_RAINBOW_MOOD
    #define RGBLIGHT_EFFECT_RAINBOW_SWIRL
    #define RGBLIGHT_EFFECT_SNAKE
    #define RGBLIGHT_EFFECT_KNIGHT
    #define RGBLIGHT_EFFECT_CHRISTMAS
    #define RGBLIGHT_EFFECT_STATIC_GRADIENT
    #define RGBLIGHT_EFFECT_RGB_TEST
    #define RGBLIGHT_EFFECT_ALTERNATING
    #define RGBLIGHT_EFFECT_TWINKLE
    #define RGBLIGHT_HUE_STEP 8
    #define RGBLIGHT_SAT_STEP 8
    #define RGBLIGHT_VAL_STEP 8
    #define RGBLIGHT_LIMIT_VAL 160 /* The maximum brightness level */
    #define RGBLIGHT_SLEEP         /* If defined, the RGB lighting will be switched off when the host goes to sleep */

#endif
