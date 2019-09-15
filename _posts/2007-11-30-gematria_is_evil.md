---
id: 93
title: "גימטרעה"
date: 2007-11-30 23:11:20
layout: post
categories: 
  - הבלים פסאודו-מתמטיים
---
ב<a href="http://www.gadial.net/?p=91">פוסט קודם</a> הזכרתי את המושג של <a href="http://he.wikipedia.org/wiki/%D7%A4%D7%95%D7%A0%D7%A7%D7%A6%D7%99%D7%99%D7%AA_%D7%92%D7%99%D7%91%D7%95%D7%91">פונקצית תמצות</a> - פונקציה שלוקחת ערכים מתחום גדול מאוד (אולי אף אינסופי) ו"מתמצתת" אותם לערכים מתחום קטן בהרבה. כשכמות הערכים מהתחום הגדול שסביר שניתקל בהם במציאות היא נמוכה (כמה סרטים "אמיתיים" יש מתוך כל הקבצים האפשריים של 700 מגה?), הסיכוי ל"התנגשות" בתמצות (שני ערכים שמתומצתים לאותה תמצית) הוא נמוך מאוד עבור פונקצית תמצות שנבחרה בחוכמה, ולכן אפשר להשתמש בתמצות בתור דרך טובה לזהות בצורה מובהקת קבצים גדולים גם בלי לקרוא את כולם. כך למשל ישנם שרתי קבצים שמספקים תמצות של הקובץ אותו רוצים להוריד (במקרה זה, תמצות באמצעות הפונקציה <a href="http://he.wikipedia.org/wiki/MD5">MD5</a>) כדי שמוריד הקובץ יוכל לוודא שאכן הוריד את הקובץ הנכון וללא שגיאות.

הפעם אני רוצה לדבר על דוגמה לפונקצית תמצות <strong>רעה</strong>, ומה קורה כשמייחסים לה חשיבות, ולו אפסית. לפונקציה הזו קוראים "<a href="http://he.wikipedia.org/wiki/%D7%92%D7%99%D7%9E%D7%98%D7%A8%D7%99%D7%94">גימטריה</a>".

גימטריה היא משחק פשוט וחביב: לכל אות בא"ב העברי מתאימים ערך מספרי: א' הוא 1, ב' הוא 2, וכן הלאה עד י' שהוא 10. אחר כך מתחילים בקפיצות של 10: כ' הוא 20, ל' הוא 30 וכן הלאה עד ק' שהוא 100. מכאן והלאה הקפיצות הן של 100, עד לת' שהוא 400 (אותיות סופיות זהות בערכן לאותיות הלא-סופיות המתאימות). הבחירה הזו אינה שרירותית - בעבר, לפני שהתחלנו להשתמש ב<a href="http://he.wikipedia.org/wiki/%D7%94%D7%A9%D7%99%D7%98%D7%94_%D7%94%D7%A2%D7%A9%D7%A8%D7%95%D7%A0%D7%99%D7%AA">שיטת כתיב המספרים</a> שאנו משתמשים בה כיום (שהיא למעשה מחוכמת למדי, וראויה לפוסט נפרד), השתמשו העברים ב<a href="http://he.wikipedia.org/wiki/%D7%A1%D7%A4%D7%A8%D7%95%D7%AA_%D7%A2%D7%91%D7%A8%D7%99%D7%95%D7%AA">אותיות עבריות</a> כדי לכתוב מספרים. כך רמ"ח אברים הם מאתיים ארבעים ושמונה, ותרי"ג המצוות הן שש מאות ושלושה-עשר. גם בימינו יש, כמובן, שימושים רבים לספרות העבריות - בפרט, לוח השנה העברי, והגימטריה.

אם כן, מהי גימטריה? מסתכלים על מילה בעברית ומתמצתים אותה לערך המספרי שלה על פי ההמרה שלעיל. כך למשל "גימטריה" עצמה היא 277. כמובן שאת 277 אפשר להציג באמצעות אותיות בדרכים רבות ושונות - הפשוטה מביניהן היא רע"ז, אך אפשר לשחק עם זה מכאן ועד להודעה חדשה. זוהי בדיוק הגימטריה - משחק. משחק שמטרתו למצוא עוד מילים שמתומצתות לאותו ערך מספרי. למשל, משחק מפורסם וחביב הוא זה של "נכנס יין, יצא סוד" - לפסוק החביב הזה מתקבלת משמעות נוספת כששמים לב שגם ל"יין" וגם ל"סוד" אותו ערך גימטרי - 70.

באנציקלופדיה היהודית האינטרנטית  "<a href="http://www.daat.ac.il/encyclopedia/value.asp?id1=1133">דעת</a>" אומרים כי הגימטריה היא אחת מהדרכים לפרשנות התורה - בדרך כלל הכוונה היא להחלפת מילה במספר, ולא במילה אחרת בעלת אותו ערך גימטרי. ככל הנראה פרשני המקרא לא התייחסו בעצמם ברצינות רבה לרעיון החלפת המילה במילה. עם זאת, עוד טוענת האנציקלופדיה כי "<span>חכמת הקבלה הרחיבה את גבול הגימטריה לבלי קץ". לא זכיתי לחזות באור חכמת הקבלה ולכן איני יודע כיצד עשתה זאת; אך כמו כל דבר שיש לו נופך מיסטי בימינו, גם הקבלה הורדה לזנות - ואיתה, הגימטריה.</span>

פעם, לפני עשר שנים לערך, גימטריות היו נפוצות למדי בויכוחי דתיים-חילונים באינטרנט. לדוגמה, אחרי הקשקוש של הרב עובדיה יוסף על כך ש"בקריאת המגילה, שעה שתגידו ארור המן תגידו גם ארור יוסי שריד" הוצדק בזריזות על ידי אלו שהבחינו כי הן "יוסף שריד" והן "המן הרשע" מתומצתים גימטרית ל-670. בזמן שירותי הצבאי (שהפגיש אותי עם קשת רחבה יחסית של האוכלוסיה) נתקלתי במספר אנשים שעדיין האמינו בנכונות מיסטית כלשהי של הגימטריה, אך עם הזמן הלכה ופחתה הרצינות שיוחסה לה, מכל חלקי הציבור, והדבר ללא ספק קשור בקשר הדוק להתפתחותם של "מחשבוני הגימטריה".

תוכנה לחישוב גימטריה היא דבר קל ביותר לכתיבה; איני יודע אם זכות הראשונים שמורה לתוכנה "<a href="http://www.hofesh.org.il/religion_merchants/gimatria/wingim1.0/wingim10.html">WinGim</a>" (כנראה שלא), אך היא הייתה הראשונה אליה שמתי לב, כך שכנראה הייתה הראשונה בעלת תפוצה רצינית, והיא הראתה עד כמה קל למצוא בגימטריה כל מה שרוצים. מאז נפוצו "מחשבוני רשת", שאינם תוכנה שיש להוריד, אלא פשוט תיבת טקסט באתר שבה אתה מקיש את המילה, ומקבל התאמות. הקושי שבכתיבת תוכנית גימטריה אינו התכנות עצמו, שהוא טריוויאלי למדי (עבור על המילה אות אות; המר כל אות למספר; סכום את המספרים; חפש מילים אחרות בעלות אותו ערך מתוך מאגר קיים), אלא בניית המילון שאיתו עובדים. לשם כך יש צורך במאגר גדול (ורצוי חופשי) של מילים בעברית, ורצוי מילים "עסיסיות". מחשבוני הרשת מסוגלים לזכור את החיפושים שהוקלדו בהם בעבר, ובכך לנפח בקלות יחסית את מאגר המילים (וחשוב יותר - הביטויים שמורכבים ממספר מילים) שלהם, ואולי זו הסיבה להצלחתם היחסית.

בימינו, אם כן, כבר לא לוקחים ברצינות את הגימטריה. היא עדיין מוזכרת בקרב <a href="http://kabbalic-numerology.jer.co.il/Front/Tools/homepage.asp">נומרולוגים למיניהם</a>, אך כמעט ולא נתקלתי בה במהלך דיון רציני, וברור שאין לה יותר את כוח השכנוע של אחותה הגדולה והמרושעת - דילוגי האותיות (אחות שראויה לפוסט נפרד ומקיף יותר).

ובכל זאת, לא הייתי הוגן לגמרי כלפי הגימטריה - טרם הסברתי <strong>למה</strong>, בעצם, זו פונקצית תמצות כל כך גרועה. התשובה, עם זאת, טריוויאלית.

אני לומד עכשיו את שפת התכנות <a href="http://he.wikipedia.org/wiki/%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F">Python</a>, וכחלק מהלימוד כתבתי תוכנת גימטריה (זהו תירוץ נהדר ללמוד כיצד ניתן לעבוד עם עברית - ובאופן כללי, <a href="http://he.wikipedia.org/wiki/%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F">יוניקוד</a> - וכיצד ניתן לכתוב <a href="http://he.wikipedia.org/wiki/GUI">GUI</a> בעזרת השפה). לצורך כך נזקקתי, כמובן, למאגר מילים חופשי בעברית. החלטתי לבסוף להשתמש במאגר של תוכנת בדיקת האיות <a href="http://en.wikipedia.org/wiki/MySpell">MySpell</a> , בשל פשטותו - כל המילים היו מאוחסנות בקובץ טקסט רגיל, שקל מאוד לקרוא ולעבד. מכיוון שזה מילון שמיועד לבדוק איות, הוא הכיל מילים ואת הטיותיהן השונות. חישבתי את הערך הגימטרי לכל מילה, ומיינתי. התברר שהמילה בעלת הערך הגימטרי הגבוה ביותר במילון היא "תשתיתיות" עם 1926. גם "תורשתיות" ו"תקשורתיות" חזק בתמונה, בין היתר. כלומר - פונקצית התמצות לוקחת מילים מתחום שגודלו טרם ידוע, ומעתיקה אותן לתחום שגודלו לא עולה על 2,000.

מה גודל התחום המקורי? יש בעברית 22 אותיות (נתעלם מאותיות סופיות). זה אומר, למשל, שיש 113,379,904 דרכים אפשריות לצרף 6 אותיות בעברית. כלומר, ברור שהתחום ה"מקורי" הוא אכן עצום בגודלו. התקווה, כזכור, היא שמספר המילים "בעלות המשמעות" שאפשר למצוא בתוך התחום הוא קטן הרבה יותר. זה כמובן נכון, אבל... המילון של MySpell מכיל בערך 330,000 מילים. זה גודל זעום לעומת מספר המילים האפשרי, אבל זה עדיין גודל עצום ביחס למספר התמציות האפשריות. זה אומר 165 מילים לתמצית, בממוצע. בפועל, כמובן שהמצב גרוע עוד יותר - רובן המוחץ של המילים הן בעלות ערכים גימטריים נמוכים יותר. מכאן נובע עוד משהו - שההתפלגות שמשרה פונקצית התמצות הזו אינה אחידה, וגם לא מתקרבת להיות אחידה. בקיצור - מובטחות לנו התנגשויות מכאן ועד להודעה חדשה, וזה בדיוק מה שקורה בפועל בגימטריה.

עד עכשיו דיברנו רק על מילים בודדות. כאן יכולת ההתחכמות שלנו היא נמוכה יחסית.  בכל זאת, אם "גימטריה" לא מתאימה מבחינת ערכה המספרי לשום מילה "עסיסית", אכלנו אותה. ברגע שאפשר להכניס צירופי מילים למשחק, פתאום הכל הופך לגמיש יותר. כך למשל אני רוצה למצוא צירוף מילים שמשווה "גימטריה" ל"בזבוז זמן". לרוע המזל, הפרש הגימטריות של "גימטריה" ושל "בזבוז זמן" הוא 156. מה עושים? מחפשים מילה שערכה הגימטרי הוא 156 ושתישמע טוב כאשר תצורף ל"בזבוז זמן"... התוכנה האומללה שלי מצאה, בין היתר, את "סיטונאיי". נו, זה לא טוב - יש י' מיותרת. מה עושים? מעבירים אותה ל"בזבוז" - מקבלים ש"גימטריה" שווה ל"ביזבוז זמן סיטונאי". מה הלך כאן?

מה שהלך כאן הוא שניצלתי את הגמישות הרבה של הגימטריה - כשאומרים לי ש"יוסף שריד"="המן הרשע", אני לא שואל את עצמי "למה 'יוסף' ולא 'יוסי'?". אני רואה רק את התוצאה הסופית, שעלולה להיראות להדיוט מוחלט כאילו היא בעלת משמעות כלשהי. אני לא רואה את כל הנסיונות הכושלים שעומדים מאחוריה - אלף ואחד דברים רעים ש"יוסי שריד" לא מתאים להם - אני רואה רק את צירוף המקרים (המשעשע) שכן התאים. ככה זה - כשהמוני צירופי מילים נכנסים לכל התאים האפשריים, משהו רע ייפול לתא של "יוסי שריד" (ואם לא - אז לתא של "יוסף שריד"). משהו רע נופל לתא של כל אחד מאיתנו - וגם משהו טוב, אגב. ואם צריך לתקן קצת כדי שיתאים, למה לא - אף אחד לא ישאל למה "ביזבוז" ולא "בזבוז".

וכאן אנחנו מגיעים לשורש העניין, שגימטריה היא רק סימפטום שולי שלו. לטיעון נפוץ מאוד בקרב מחזירים בתשובה - "טיעון הסיכוי הנמוך": אם מתקיים משהו ש<strong>נראה לנו</strong> שההסתברות שלו נמוכה, אנו נוטים לייחס לו משמעות. יוסף שריד זה המן הרשע? כנראה שזה אומר משהו. דילוגי אותיות בתורה מנבאים את נפילת מגדלי התאומים? כנראה שהתורה נכתבה בידי כוח עליון. חשבנו על מישהו והוא התקשר? כנראה יש טלפתיה. הרי מה הסיכוי שהדברים הללו יקרו במקרה? ומכאן, לטיעון המחץ הבסיסי ביותר: ההסתברות שאדם יווצר "במקרה" היא אפסית? כנראה שיד מכוונת יצרה אותו.

בכוונה הפרדתי את שלושת הטיעונים הראשונים מהאחרון. האחרון פשוט שגוי כי האדם לא נוצר "במקרה" - אבל זה כבר שייך לדיון על <a href="http://he.wikipedia.org/wiki/%D7%90%D7%91%D7%95%D7%9C%D7%95%D7%A6%D7%99%D7%94">אבולציה</a>. שלושת הראשונים, שבהם אני עוסק כרגע, הם דוגמאות נאות לצורה שבה מאורע בהסתברות נמוכה מתרחש פשוט כי חוזרים על אותה "הטלת מטבע" הרבה פעמים - במקרה של הטלפתיה, אנחנו חושבים על אנשים כל הזמן, ואנשים מתקשרים אלינו כל הזמן - כל מאורע כזה הוא "טלפתיה" פוטנציאלית. פעם ב- שני האירועים הללו משתלבים זה בזה, ואז אנחנו מתפלאים. באותה מידה, אפשר להתפלא על קבלת 6-6-6 בהטלת שלוש קוביות שמתבצעת כל הזמן. את כל זה ניסח הרבה לפני, בצורה הומוריסטית, המתמטיקאי ג'ון ליטלווד, ב"<a href="http://he.wikipedia.org/wiki/%D7%97%D7%95%D7%A7_%D7%9C%D7%99%D7%98%D7%9C%D7%95%D7%95%D7%93">חוק ליטלווד</a>" שקובע שאדם יכול לצפות לנסים בקצב של אחד לחודש בערך.

בגימטריה ודילוגי אותיות הסיטואציה פחות ברורה. לכאורה, הכל כבר נתון מראש - אנחנו לא "מגרילים" גימטריה של מילים - היא פשוט קיימת, וזהו. גם התנ"ך כבר קיים, והוא לא טקסט שמוגרל שוב ושוב. לטעמי, ההבדל אינו מהותי, אך את הדיון הזה אשמור כנראה לפוסט שיעסוק בדילוגי אותיות - שהם, כאמור, רעה חולה גדולה בהרבה מהגימטריה החביבה והמסכנה.

ומה המסקנה מכל זה, לדעתי? שאפשר ואף רצוי להשתעשע בגימטריה (די מהר זה נמאס); אבל אם בדיון רציני מישהו שולף גימטריה, ותהא הסיבה אשר תהא - אפשר לסיים את הדיון בו במקום. גרוע יותר מ<a href="http://he.wikipedia.org/wiki/%D7%97%D7%95%D7%A7_%D7%92%D7%95%D7%93%D7%95%D7%95%D7%99%D7%9F">גודווין</a>.