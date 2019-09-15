---
id: 633
title: "כל כך קשה לבחור..."
date: 2010-07-08 14:32:07
layout: post
categories: 
  - קומבינטוריקה
tags: 
  - מתמטיקה תיכונית
  - קומבינטוריקה
---
אני ממשיך את סדרת הפוסטים שלי על קומבינטוריקה ברמה תיכונית, והפעם אני רוצה לנקוט בגישה "מתמטית" לדברים שכבר גילינו. המתמטיקאי תמיד מנסה לבחון מחדש את ההנחות שלו ולהקל על הדרישות בכדי להכליל את התוצאות שלו, וזה גם מה שאני רוצה לעשות. הנוסחה המרכזית ש<a href="http://www.gadial.net/?p=534">גילינו</a> עד כה הייתה כי {% equation %}\frac{n!}{k!\left(n-k\right)!}{% endequation %}, שאותו סימנו בקיצור {% equation %}{n \choose k}{% endequation %} וכינינו "מקדם הבינום"(מסיבות שהסברתי בפוסט קודם) הוא מספר הדרכים לבחור {% equation %}k{% endequation %} מתוך {% equation %}n{% endequation %} עצמים. אלא שכאן יש לי שתי הנחות סמויות: שהבחירה היא ללא החזרה, וללא חשיבות לסדר. בפוסט הזה אנסה להסביר מה זה אומר, ומה מקבלים כשמשחקים עם ההנחות הללו.

בואו נזכור מה {% equation %}{n \choose k}{% endequation %} אומר באמצעות דוגמה: בלוטו, אם נשכח לרגע מהמספר הנוסף, נבחרים שישה מספרים מתוך 49. הבחירה הזו היא ללא חשיבות לסדר: אם המכונה הגרילה קודם כל את 1 ואז את 2, זו אותה הסיטואציה מבחינתנו כמו זו שבה המכונה הגרילה קודם כל את 2 ורק אז את 1. די ברור שאם הייתה חשיבות לסדר, המשחק היה הופך לקשה פי כמה, כי לא היה מספיק לנחש <strong>מי</strong> יזכה; היה צריך לנחש גם <strong>באיזה סדר</strong> הם יופיעו.

הבחירה שבלוטו היא גם ללא החזרות: אם המכונה הגרילה 1, זהו זה מבחינת המספר 1 - לא ייתכן שהוא ייבחר שוב. אפשר היה לחשוב על הגרלה שמתנהלת אחרת - אם מוגרל כדור הוא מוצג לצופים, ומייד אחר כך מוחזר אל בריכת הכדורים, כך שייתכן שהוא ייבחר שוב. גם סיטואציה כזו היא בבירור יותר קשה עבורנו מסתם בחירת שישה מספרים - אנחנו נצטרך גם לחשוב על סיטואציות שבהן אותו מספר נבחר כמה פעמים. למעשה, בלתי נתפס אינטואיטיבית ככל שיהיה, בסיטואציה שכזו התוצאה {% equation %}1,1,1,1,1,1{% endequation %} סבירה <strong>בדיוק כמו כל תוצאה אחרת</strong> (אגב, האם מישהו מכם מרגיש "מוזר"להמר על תוצאה כמו {% equation %}1,1,1,1,1,1{% endequation %} אבל תוצאות אחרות הן בסדר מבחינתו? זו המחשה לאופן שבו האינטואיציה שלנו מטעה אותנו לחלוטין במשחקי מזל שכאלו, ולכן הם כה פופולריים).

הנה תרגיל בקומבינטוריקה: אם סוגי הבחירות השונות נקבעים לפי השאלות א) האם יש חשיבות לסדר או לא ו-ב) האם יש החזרה או לא, כמה סוגי בחירות יש? התשובה היא כמובן 4 (מעקרון הכפל). הבה ונטפל בכולן. בכל המקרים יהיה מדובר על בחירה של {% equation %}k{% endequation %} אובייקטים כשיש {% equation %}n{% endequation %} אובייקטים לבחור מהם.

ובכן, בחירה בלי החזרה ובלי חשיבות לסדר היא כמו שראינו {% equation %}{n \choose k}{% endequation %}. לפעמים משתמשים גם בסימון המבלבל {% equation %}C_{n}^{k}{% endequation %} וקוראים לזה "צירופים", אך זה הרבה פחות מקובל במתמטיקה ואני לא משתמש בסימונים הללו אף פעם.

נעבור לבחירה בלי החזרה אך עם חשיבות לסדר, מה שנקרא לעתים בעברית "חליפות"ומסומן ב-{% equation %}A_{n}^{k}{% endequation %}. הדרך לחשב את מספר האפשרויות לבחור בלי החזרה ועם חשיבות לסדר {% equation %}k{% endequation %} מתוך {% equation %}n{% endequation %} עצמים היא פשוטה למדי כי אפשר לחשוב עליה כתהליך דו-שלבי: קודם כל נבחר {% equation %}k{% endequation %} עצמים מתוך ה-{% equation %}n{% endequation %} בלי חשיבות לסדר, ואז נבחר את האופן שבו "מסדרים"אותם. כבר ראינו שיש {% equation %}{n \choose k}{% endequation %} אפשרויות לבחור את העצמים בלי חשיבות לסדר, ושבהינתן {% equation %}k{% endequation %} עצמים יש {% equation %}k!{% endequation %} דרכים לסדר אותם, כך שהתוצאה היא {% equation %}{n \choose k}k!=\frac{n!}{k!\left(n-k\right)!}k!=\frac{n!}{\left(n-k\right)!}{% endequation %}. אפשר גם להגיע לתוצאה הזו בדרך ישירה: בהתחלה יש לנו {% equation %}n{% endequation %} איברים לבחור מהם, אחר כך יש לנו {% equation %}n-1{% endequation %} איברים, אחר כך {% equation %}n-2{% endequation %} וכן הלאה... עד שבסופו של דבר יש לנו {% equation %}n-k{% endequation %} איברים ואז אנחנו כבר לא בוחרים. נקבל את המכפלה {% equation %}n\cdot\left(n-1\right)\cdot\left(n-2\right)\cdots\left(n-k+1\right){% endequation %} (ה-{% equation %}+1{% endequation %} בסוגר האחרון נובע מכך שהבחירה האחרונה מתבצעת רגע לפני שאנו נשארים עם {% equation %}n-k{% endequation %} איברים) - לא קשה לראות שמכפלה זו אכן שווה ל-{% equation %}\frac{n!}{\left(n-k\right)!}{% endequation %}, אבל היא יותר מסורבלת לכתיבה. שימו לב, אגב, שאם היינו בוחרים {% equation %}k=n{% endequation %} היינו מקבלים את התוצאה {% equation %}n!{% endequation %} - כלומר, הכללנו גם את הרעיון של סידור {% equation %}n{% endequation %} איברים בשורה.

אני רוצה להציג עוד נקודת מבט שתכליל הן את הצירופים והן את החליפות, ותיתן לנו עוד נוסחה מאוד פופולרית. בואו נחשוב לרגע שיש לנו {% equation %}n{% endequation %} כדורים, ש-{% equation %}k{% endequation %} מתוכם אדומים והיתר כחולים, ואנחנו שואלים את עצמו בכמה דרכים ניתן לסדר אותם בשורה. שימו לב שכל הכדורים מאותו צבע נראים לנו זהים - אם נחליף את המקומות של שני כדורים בעלי אותו צבע נקבל תוצאה שנראית לנו זהה לקודמת, ולכן אין צורך לספור אותה שוב. מה עושים? דרך אחת היא זו: ראשית נחשוב על כל הכדורים כעל אובייקטים שונים זה מזה, ואז יש {% equation %}n!{% endequation %} דרכים שונות לסדר אותם בשורה. כעת צריך "לתקן"את הספירות הכפולות שביצענו, והדרך לעשות זאת היא לספור בכמה דרכים שונות ניתן לשנות את הסדר הפנימי בין הכדורים האדומים, ובכמה דרכים שונות ניתן לשנות את הסדר הפנימי בין הכדורים הכחולים, ולחלק בתוצאה זו. יש {% equation %}k{% endequation %} כדורים אדומים ולכן {% equation %}k!{% endequation %} סידורים פנימיים שלהם, ובאופן דומה יש {% equation %}\left(n-k\right)!{% endequation %} סידורים פנימיים של הכדורים הכחולים, ולכן התוצאה היא {% equation %}\frac{n!}{k!\left(n-k!\right)}{% endequation %} - בדיוק {% equation %}{n \choose k}{% endequation %} וזה לא כל כך מפתיע כי אפשר לחשוב על הסידור הנ"ל כעל "בחר {% equation %}k{% endequation %} מקומות עבור הכדורים האדומים ושים את הכחולים ביתר". למעשה, הגישה הזו הייתה האופן שבו הוכחתי את הנוסחה עבור {% equation %}{n \choose k}{% endequation %} מלכתחילה.

כעת להכללה המבוקשת - מה קורה אם יש לי כדורים אדומים, ירוקים, צהובים וכחולים? ומה אם יש עוד צבעים? באופן כללי אפשר לחשוב על כך ש-{% equation %}n{% endequation %} האיברים מתחלקים לקבוצות, כך שמספרי האיברים בקבוצות הם {% equation %}k_{1},k_{2},\dots,k_{t}{% endequation %}. קבוצה יכולה להכיל גם איבר בודד; לכן אנחנו יכולים להניח שה-{% equation %}k{% endequation %}-ים מתארים את כל האיברים, כלומר מתקיים {% equation %}n=k_{1}+k_{2}+\dots+k_{t}{% endequation %}. על פי אותו הגיון שתיארתי קודם, מספר הסידורים האפשריים בשורה של האיברים הללו, כשאנחנו מתעלמים מהסידורים הפנימיים בין איברים מאותו צבע, הוא {% equation %}\frac{n!}{k_{1}!k_{2}!\cdots k_{t}!}{% endequation %}. שימו לב ש-{% equation %}{n \choose k}{% endequation %} מתאים למקרה בו יש לנו בדיוק שתי קבוצות, ואילו מספר החליפות, {% equation %}\frac{n!}{\left(n-k\right)!}{% endequation %} מתאים בדיוק למקרה שבו יש לנו {% equation %}n-k{% endequation %} עצמים זהים והיתר שונים זה מזה (כך שהנוסחה היא בעצם {% equation %}\frac{n!}{\left(n-k\right)!1!1!\cdots1!}{% endequation %} ואין צורך לכתוב את ה-{% equation %}1{% endequation %}-ים במכנה כי {% equation %}1!=1{% endequation %}). למה הסיטואציה הזו אכן מתארת חליפות? כי ניתן לחשוב על כך שאנחנו מניחים על העצמים שלנו פתקים שבהם או שכתוב מספר כלשהו מ-{% equation %}1{% endequation %} עד {% equation %}k{% endequation %} (שמתארים את מספרם בבחירה) או שכתוב עליהם "לא נבחר", וכל פתקי ה"לא נבחר" זהים זה לזה ויש {% equation %}n-k{% endequation %} מהם.

טוב, אז זה מסיים את עניין הבחירה בלי החזרות. הבה ונעבור לבחירה עם החזרות - שימו לב שכאן {% equation %}k{% endequation %} יכול להיות גדול מ-{% equation %}n{% endequation %} כי האיברים לא יכולים "להיגמר" לנו. הסיטואציה כאן מאוד מעניינת - מצד אחד, אם יש חשיבות לסדר הנוסחה פשוטה ביותר (כה פשוטה שאני ממליץ לכם לנסות ולהמציא אותה לבד לפני שתקראו מה שאכתוב). מצד שני, הנוסחה עבור בחירה עם החזרות אך בלי חשיבות לסדר היא קשה יחסית - כה קשה שאיני חושב שמלמדים אותה כלל בתיכון, אפילו אם כן לומדים קומבינטוריקה. למרות זאת הדגש צריך להיות על הקושי ה<strong>יחסי</strong>: הנוסחה אינה נוראית כלל ואני מקווה שעד סיום הפוסט יוכלו כל הקוראים לפתח אותה בעצמם.

הנוסחה לבחירה עם החזרה ועם חשיבות לסדר היא תוצאה ישירה של עקרון הכפל. תהליך הבחירה שלנו הוא בן {% equation %}k{% endequation %} שלבים; בכל שלב אנחנו בוחרים אחת מ-{% equation %}n{% endequation %} אפשרויות שונות. יש לנו אם כן בסך הכל {% equation %}n\cdot n\cdots n=n^{k}{% endequation %} אפשרויות שונות. קל להתבלבל ולשכוח מי במעריך החזקה ומי בבסיס (כלומר, האם זה {% equation %}k^{n}{% endequation %} או {% equation %}n^{k}{% endequation %}) ולכן אני ממליץ לנקוט בגישה הבאה: כמה מספרים דו ספרתיים יש, אם מרשים גם לאפס להופיע (כלומר, {% equation %}3{% endequation %} הוא המספר ה"דו ספרתי" {% equation %}03{% endequation %} וכדומה)? {% equation %}2^{10}{% endequation %} או {% equation %}10^{2}{% endequation %}? ובכן, {% equation %}2^{10}=1024{% endequation %} כך שברור שיש כאן בעיה; לעומת זאת {% equation %}10^{2}{% endequation %} מתאים בדיוק, וזה לא מפתיע כי מספר דו ספרתי מורכב מבחירה של אחת מ-10 הספרות האפשריות בתור ספרת האחדות, ואחת מ-10 הספרות האפשריות בתור ספרת העשרות.

נעבור לבחירה עם החזרה ו<strong>בלי</strong> חשיבות לסדר. גם כאן כדאי לנסות ולחפש את הנוסחה המתאימה באופן עצמאי קודם; זה מאפשר לראות את ה"קושי"שיש כאן בהשוואה למקרים האחרים. הפתרון שאציע הוא דרך שיטת העבודה הסטנדרטית במתמטיקה - הכנת תה. הסיפור מספר על מתמטיקאי ופיזיקאי שמתבקשים להכין לעצמם תה. הפיזיקאי לוקח את קומקום המים הריק, ממלא אותו במים, מרתיח, שופך מקצת המים לכוס ומכין לעצמו. בא המתמטיקאי, לוקח את הקומקום שעדיין מלא, מרוקן את תוכנו לכיור ואומר "עכשיו חזרנו לבעיה שאותה אנחנו כבר יודעים לפתור". כך גם כאן - נעבור לבעיה שאותה אנחנו כבר יודעים לפתור - בחירה <strong>בלי</strong> החזרה ובלי חשיבות לסדר.

הדרך הנוחה ביותר לתאר זאת היא באמצעות סיפור מעשיות. בחירה של {% equation %}k{% endequation %} מתוך {% equation %}n{% endequation %} איברים ללא חשיבות לסדר ועם החזרה ניתן לתאר בתור סידור כדורים בתאים: נניח שיש לנו שורה של {% equation %}n{% endequation %} תאים ממוספרים, ו-{% equation %}k{% endequation %} כדורים זהים. אנחנו זורקים כדורים לתוך התאים ובסוף רואים מה קיבלנו. אם בתא מס' 1 יש שני כדורים, אנחנו אומרים שבחרנו את האיבר מס' 1 בדיוק שתי פעמים; אם בתא 2 אין כדורים כלל אנו אומרים שאת איבר מס' 2 בכלל לא בחרנו, וכן הלאה.

עכשיו בואו ונהפוך את הקערה על פיה. בואו נדמיין שאין בכלל תאים אלא רק תא אחד ארוך מאוד. ושכל הכדורים כבר מסודרים בו בשורה כמו ילדים טובים. ואז אנחנו באים ובין זוג כדורים כלשהו שמים <strong>מחיצה</strong> שמחלקת את התא לשני תאים. מה שעשינו בפועל הוא לחלק את הכדורים בין <strong>שני</strong> תאים - שני התאים שנוצרו לאחר ששמנו את המחיצה. אם למשל אשים את המחיצה בדיוק באמצע התא אחלק את הכדורים שווה בשווה בין שני התאים; ואם אשים את המחיצה מימין לכדור הימני ביותר, ממש בינו ובין הקיר, אצור תא רק ותא אחר שמכיל את כל הכדורים. אם כן, זה המשחק שאני רוצה לעשות, רק עם {% equation %}n-1{% endequation %} מחיצות (שאחרי שאכניס ייצרו {% equation %}n{% endequation %} תאים).

בגישה הזו מה שאני "בוחר" הוא את המקומות שבהם אני רוצה לשים את המחיצות. על פניו כל רווח בין שני כדורים, או בין כדור והקיר, הוא מיקום חוקי. יש {% equation %}k{% endequation %} כדורים ולכן {% equation %}k+1{% endequation %} רווחים (ציירו שני כדורים ותראו את שלושת הרווחים: מימין לכדור הימני, משמאל לשמאלי, ובין שניהם). לכן יש לי בחירה של {% equation %}n-1{% endequation %} איברים מתוך קבוצה של {% equation %}k+1{% endequation %} איברים, בלי חשיבות לסדר ועם החזרה, כי אפשר לבחור באותו רווח כמה פעמים... היי, רגע, אז מה בעצם השגתי כאן? אני עדיין תקוע עם בעיה של בחירה עם החזרה ולא שיפרתי כלום!

אם לגלוש לרגע למתמטיקה יותר מתקדמת, כשכזה דבר קורה זה לא בהכרח סוף העולם. אפשר לחזור על אותו תהליך שוב ושוב ולראות האם זה הופך את הבעיה בהדרגה לפשוטה יותר. לרוע המזל, זה לא מה שקורה כאן - מבעיה של בחירת {% equation %}k{% endequation %} מתוך {% equation %}n{% endequation %} עברתי לבעיה של בחירת {% equation %}n-1{% endequation %} מתוך {% equation %}k+1{% endequation %}, ואם אעשה את התעלול שוב אחזור לבעיה של בחירת {% equation %}k{% endequation %} מתוך {% equation %}n{% endequation %}. צריך להוסיף עוד תעלול לתמונה, אם כך. והתעלול הזה פשוט - אני הולך לאסור על תאים ריקים.

הטענה שלי היא כזו: מספר הדרכים השונות לחלק {% equation %}k{% endequation %} כדורים ל-{% equation %}n{% endequation %} תאים (בלי חשיבות לסדר) שווה בדיוק למספר הדרכים השונות לחלק {% equation %}n+k{% endequation %} כדורים ל-{% equation %}n{% endequation %} תאים כשבסוף החלוקה אין תאים ריקים. למה? זה פשוט: כי נתחיל את החלוקה בלשים כדור אחד בכל תא. כך הבטחנו שמה שחייב להתקיים, מתקיים, ואז {% equation %}k{% endequation %} הכדורים שנותרו אפשר לחלק בשקט ובלי מגבלות כלשהן. אם כן, המרנו את הבעיה שלנו לבעיה אחרת, שאותה יהיה לנו קל יותר לתקוף.

נחזור לבעיית השמת המחיצות. אם אסור שיהיו תאים ריקים, זה אומר שאסור לשים שתי מחיצות בין אותו זוג כדורים, ואסור לשים מחיצה בין כדור ובין הקיר. מצד שני, יש לנו הפעם {% equation %}n+k{% endequation %} כדורים, ולכן יש בסך הכל {% equation %}n+k-1{% endequation %} רווחים שבהם ניתן לשים את {% equation %}n-1{% endequation %} המחיצות. הפעם הבחירה היא <strong>בלי</strong> החזרות כי כאמור, אסור לשים שתי מחיצות בין אותו זוג כדורים - אסור לבחור פעמיים באותו רווח שבין כדורים. לכן יש לנו בחירה של {% equation %}n-1{% endequation %} איברים מתוך {% equation %}n+k-1{% endequation %} איברים, וזה בדיוק {% equation %}{n+k-1 \choose n-1}{% endequation %}, ואת זה ניתן לכתוב גם כ-{% equation %}{n+k-1 \choose k}{% endequation %}. בזאת מצאנו את הנוסחה לשיטת החלוקה הרביעית והאחרונה.

לפני שנסיים להפעם אני רוצה לתאר שימוש פשוט אחד בבחירה עם החזרה ובלי חשיבות לסדר, שבינתיים אולי נראית מפחידה ומסובכת ולא מועילה כלל. נביט במשוואה {% equation %}x_{1}+x_{2}+\dots+x_{n}=k{% endequation %}, כאשר {% equation %}k{% endequation %} הוא מספר שלם והערכים שאנחנו מרשים למשתנים לקבל הם רק ערכים שלמים אי שליליים (משוואות כאלו צצות בפועל! בעולם האמיתי! תאמינו לי!). כמה פתרונות יש למשוואה הזו? בדיוק מספר האפשרויות לבחור {% equation %}k{% endequation %} איברים מתוך {% equation %}n{% endequation %}, עם החזרה ובלי חשיבות לסדר. למה? אשאיר זאת כתרגיל לקורא.