---
id: 2385
title: "לוגיקה מסדר ראשון - כמה תוצאות של משפט השלמות"
date: 2013-03-21 09:07:36
layout: post
categories: 
  - לוגיקה
tags: 
  - אקסיומות פיאנו
  - לוגיקה מסדר ראשון
  - מודלים לא סטנדרטיים
  - משפט הקומפקטיות
  - משפט השלמות של גדל
  - משפט לוונהיים-סקולם
  - פרדוקס סקולם
---
<a href="http://www.gadial.net/2013/02/26/godel_completeness_proof_2/">בפוסט הקודם </a>שלי על לוגיקה סיימתי להציג את ההוכחה של משפט השלמות ללוגיקה מסדר ראשון. בפוסט הזה אני רוצה להציג כמה מסקנות ממנו שהן (לטעמי) מאוד לא מובנות מאליהן. נתחיל עם מה שקיבלנו באותו האופן גם בתחשיב הפסוקים: קומפקטיות. משפט הקומפקטיות ללוגיקה מסדר ראשון אומר שקבוצת פסוקים כלשהי {% equation %}\Phi{% endequation %} היא ספיקה - כלומר, קיים מודל שמספק את כל הפסוקים ב-{% equation %}\Phi{% endequation %} בו זמנית - אם ורק אם כל תת-קבוצה <strong>סופית</strong> של {% equation %}\Phi{% endequation %} היא ספיקה.

ההוכחה של משפט הקומפקטיות היא טריוויאלית אם כבר יש לנו את משפט השלמות; משפט השלמות אומר ש-{% equation %}\Phi{% endequation %} היא ספיקה אם ורק אם היא עקבית. עקביות היא תכונה "סופית" במהותה - אם {% equation %}\Phi{% endequation %} אינה עקבית, אז קיימת הוכחה מתוך {% equation %}\Phi{% endequation %} של דבר והיפוכו, אבל שתי ההוכחות הללו הן שתיהן <strong>סופיות</strong> באורכן, ולכן משתמשות רק במספר <strong>סופי</strong> של הנחות מתוך {% equation %}\Phi{% endequation %}, ולכן קיימת תת-קבוצה <strong>סופית</strong> של {% equation %}\Phi{% endequation %} שאיננה עקבית. במילים אחרות, {% equation %}\Phi{% endequation %} עקבית אם ורק אם כל תת-קבוצה <strong>סופית</strong> שלה עקבית, ובשל השקילות בין עקביות ובין ספיקות קיבלנו את משפט הקומפקטיות.

במבט ראשון המשפט הזה לא נראה מעניין בכלל. אוקיי, אז קבוצות פסוקים מסויימות מקיימות איזו תכונת ספיקות לא ברורה. למי אכפת? לכן אני רוצה לפתוח עם מסקנה פשוטה לדוגמה מהמשפט. במקום להגיד מראש מה אני הולך לעשות אני פשוט אתחיל לעשות את זה והתוצאה תהיה הפתעה.

בואו נדבר על אקסיומות פיאנו. לא יהיה לי צורך בכך ולכן אני לא באמת אציג אותן כאן במפורש - זה ראוי לפוסט נפרד - אבל אסביר בקצרה מהן. אקסיומות פיאנו הן נסיון <strong>למדל</strong> את המספרים הטבעיים - כלומר, לתת תורה מסדר ראשון (אוסף של אקסיומות) כך שהמספרים הטבעיים הם מודל שלהם. המילון של אקסיומות פיאנו כולל את סימן הקבוע {% equation %}0{% endequation %} ואת סימן הפונקציה {% equation %}S{% endequation %}, שבפרשנות הסטנדרטית של האקסיומות (כלומר, זו שנמצאת לנו בראש כשאנו מגדירים את האקסיומות) תתפרש להיות פונקציית ה<strong>עוקב</strong>, כלומר {% equation %}S\left(n\right)=n+1{% endequation %}. כמו כן יש לנו את סימן היחס {% equation %}&lt;{% endequation %} שבפרשנות הסטנדרטית יתפרש להיות יחס הסדר הרגיל. יש גם סימני חיבור וכפל אבל לא נזדקק להם אז לא אציג אותם. גם לא אציג את האקסיומות עצמן במפורש - אשמור את זה לפוסט ייעודי עליהן.

הרעיון בכך שאקסיומות פיאנו "ממדלות" את המספרים הטבעיים הוא שכל מה שניתן להוכיח מאקסיומות פיאנו באמצעות מערכת ההוכחה של לוגיקה מסדר ראשון הוא בפרט נכון עבור המספרים הטבעיים (זו תכונת ה<strong>נאותות</strong> של מערכת ההוכחה). האם זה אומר שאפשר יהיה להוכיח <strong>כל</strong> טענה שנכונה על המספרים הטבעיים מתוך אקסיומות פיאנו? למרבה הצער, לא. ייתכן שזה נשמע כמו משהו שסותר את תכונת ה<strong>שלמות</strong> שהוכחתי זה עתה, אבל צריך להבין מה היא אומרת: היא אומרת שמערכת ההוכחה שלנו מאפשר לנו לגזור סינטקטית מתוך אקסיומות פיאנו את כל מה ש<strong>נובע לוגית</strong> מתוכן; זה לא אומר שכל טענה על המספרים הטבעיים נובעת לוגית מתוך אקסיומות פיאנו. ה"חולשה" כאן היא לא במערכת ההוכחה; היא באקסיומות עצמן.

מתי כן היה מובטח לנו שאפשר לגזור מאקסיומות פיאנו את כל הטענות שנכונות עבור הטבעיים (ורק אותן)? אם הטבעיים היו המודל ה<strong>יחיד</strong> של האקסיומות, כי אז כל טענה שנכונה בטבעיים הייתה נובעת לוגית מהאקסיומות בודאות. כלומר, אם יש בעיה, היא נובעת מכך שיש מודל ש"לא התכוונו אליו" שעדיין מתאים לאקסיומות פיאנו - <strong>מודל לא סטנדרטי</strong> של הטבעיים. זה לכשעצמו עדיין לא אומר שאין תקווה לכך שהאקסיומות יוכיחו את כל הטענות הנכונות עבור הטבעיים (אסביר זאת בהמשך), אבל זה כן אומר שהאקסיומות מתארות משהו יותר כללי ממה שהתכוונו אליו.

מה שאני רוצה לעשות עכשיו הוא להוכיח שיש לאקסיומות פיאנו מודל לא סטנדרטי שכזה, ואעשה את זה באמצעות משפט הקומפקטיות. ספציפית, אני רוצה להוסיף מודל שבו יהיה "מספר" שגדול מכל מספר טבעי. לצורך כך, שימו לב קודם כל לכך שאני יכול לייצג כל מספר טבעי באמצעות <strong>שם עצם</strong>: הקבוע {% equation %}0{% endequation %} מייצג את המספר אפס, שם העצם {% equation %}S\left(0\right){% endequation %} מייצג את 1, {% equation %}S\left(S\left(0\right)\right){% endequation %} מייצג את 2, וכן הלאה. במקום להסתרבל ולכתוב {% equation %}S^{n}\left(0\right){% endequation %} פשוט אכתוב {% equation %}n{% endequation %} כדי לייצג את שם העצם עבור המספר הטבעי {% equation %}n{% endequation %}.

כעת <strong>ארחיב</strong> את המילון של אקסיומות פיאנו ואוסיף סימן קבוע חדש, {% equation %}c{% endequation %}. כמו כן ארחיב את מערכת האקסיומות עצמה על ידי הוספה של אינסוף אקסיומות: הפסוקים {% equation %}c&gt;n{% endequation %} לכל {% equation %}n{% endequation %} טבעי. מודל למערכת האקסיומות המורחבת חייב לקיים את כל האקסיומות של פיאנו, ולכן להיות מודל לאקסיומות פיאנו; ו<strong>בנוסף לכך</strong> הוא חייב להכיל איבר ש-{% equation %}c{% endequation %} יותאם לו, ואותו איבר יהיה חייב להיות גדול מכל מספר טבעי {% equation %}n{% endequation %}. בבירור, המספרים הטבעיים <strong>אינם</strong> מודל של המערכת המורחבת הזו; אבל איך נוכיח שיש לה מודל כלשהו?

כאן משפט הקומפקטיות נחלץ לעזרתנו. כדי להוכיח שלמערכת המורחבת יש מודל, מספיק להראות שלכל <strong>תת קבוצה סופית</strong> שלה יש מודל. תת קבוצה סופית שכזו כוללת פסוקים אלו ואחרים מתוך אקסיומות פיאנו שלא מעניינים אותנו, ובנוסף לכך היא כוללת מספר <strong>סופי</strong> של פסוקים מהצורה {% equation %}c&gt;n{% endequation %}. בואו נסמן ב-{% equation %}N{% endequation %} את הערך המקסימלי של {% equation %}n{% endequation %} שמופיע באחד מהפסוקים הללו; עכשיו אני יכול לתת מודל לתת-הקבוצה הסופית. המודל הזה יהיה פשוט המספרים הטבעיים, {% equation %}\mathbb{N}{% endequation %}, עם הפרשנות הרגילה לסימן הקבוע 0 ולסימני הפונקציות והיחסים השונים; הדבר היחיד שאני צריך לומר במפורש הוא איך יפורש סימן הקבוע {% equation %}c{% endequation %}; אני פשוט אתאים לו את המספר הטבעי {% equation %}N+1{% endequation %}. מכיוון שהמספר הזה גדול מכל {% equation %}n{% endequation %} שמקיים {% equation %}n\le N{% endequation %}, הרי שכל פסוק מהצורה {% equation %}c&gt;n{% endequation %} ששייך לתת-הקבוצה הסופית של הפסוקים שלנו אכן מתקיים במודל שהצעתי. קיבלתי שלכל תת-קבוצה סופית של האקסיומות קיים מודל, ולכן קיים מודל לכולן (לא שברור למישהו איך הוא נראה...). סוף הסיפור.

אני חושב שזו תוצאה מדהימה. היא טריוויאלית לחלוטין בכל הנוגע להוכחה שלה, בהינתן שכבר יש לנו את משפט הקומפקטיות, ועם זאת המסקנה שלה היא משהו שנראה לי רחוק מאוד מלהיות מובן מאליו. שימו לב שנמנעתי בכוונה מלציין את אקסיומות פיאנו כדי שיהיה ברור עד כמה התוצאה שלי כללית; אין בעצם לאקסיומות פיאנו שום כלי "להתגונן" נגד התוצאה הזו של משפט הקומפקטיות, וכך גם לכל נסיון אחר למדל את הטבעיים. עוד דבר מעניין הוא שהבעיה הזו היא תוצר נלווה של העובדה שללוגיקה מסדר ראשון יש מערכת הוכחה נאותה ושלמה, מה שגורר את משפט הקומפקטיות; בלוגיקה מסדר שני קיים ניסוח של אקסיומות פיאנו שהמספרים הטבעיים הם אכן המודל היחיד שלו! רק מה, ללוגיקה מסדר שני אין בכלל מערכת הוכחה שלמה ונאותה.

בואו ונעשה תעלול דומה, אבל באופן קצת יותר חיובי, עבור המספרים הממשיים. בואו ניקח מילון פסיכי - לכל מספר ממשי {% equation %}r\in\mathbb{R}{% endequation %} יהיה בו סימן קבוע {% equation %}c_{r}{% endequation %}, ולכל יחס אפשרי על הממשיים יהיה בו סימן עבור היחס הזה. בנוסף בואו ניקח בתור אקסיומות את <strong>כל</strong> הפסוקים מעל המילון הזה שנכונים בממשיים. במובן מסויים קיבלנו תורה ש"מתארת באופן מושלם" את הממשיים. אבל האם היא חומקת ממשפט הקומפקטיות? שוב, לא; נוסיף לה סימן קבוע חדש {% equation %}c{% endequation %} ואת הפסוקים {% equation %}c_{r}&lt;c{% endequation %} לכל {% equation %}r\in\mathbb{R}{% endequation %}, ומשפט הקומפקטיות שוב יראה שיש לתורה הזו מודל שבו יש מספר שגדול מכל מספר ממשי.

עד כאן, אין חדש. אבל זכרו שהתורה שלי הייתה "כל המשפטים שנכונים בממשיים". בפרט אחד מהמשפטים הללו הוא "לכל מספר שונה מאפס יש הופכי כפלי". זה אומר שאותו איבר אינסופי שלנו הוא <strong>הפיך</strong> במודל החדש. ההופכי שלו בוודאי לא יכול להיות מספר ממשי, אז במודל החדש שלנו יש, בנוסף למספרים "אינסופיים" בגודלם, גם מספרים <strong>קטנים לאין שיעור</strong>; קטנים מכל מספר ממשי. במילים אחרות, הוכחנו את קיומם של <strong>אינפיניטסימלים</strong>, אותם מספרים שניוטון ולייבניץ השתמשו בהם בחופשיות בחדו"א שלהם ובמאה ה-19 עבדו קשה כדי לסלק אותם ממנו.

הרעיון הזה הוא השלב הראשון בדרך אל מה שנקרא <strong>אנליזה לא סטנדרטית</strong> - תחום שבו בונים את החדו"א מחדש בעזרת אינפיניטסימלים שכאלה (הנה הגדרה אלטרנטיבית לגבול: {% equation %}\lim_{x\to x_{0}}f\left(x\right)=L{% endequation %} אם כאשר {% equation %}\left|x-x_{0}\right|{% endequation %} הוא אינפיניטסימלי, כך גם {% equation %}\left|f\left(x\right)-L\right|{% endequation %}), אבל כשעושים את זה ברצינות צריך לגשת לנושא בצורה קונסטרוקטיבית יותר ואני לא הולך לעשות את זה כרגע. עצם העובדה שמשפט הקומפקטיות הופך את הוכחת ההיתכנות של אנליזה לא סטנדרטית לטריוויאלית זו תוצאה מספיק מלהיבה עבורי לפוסט הזה.

בואו נעבור למשהו אחר שגם הוא נובע ממשפט השלמות. נניח שהמילון שלנו איננו פסיכי - הוא מכיל מספר בן מניה לכל היותר של סימנים. כעת, זכרו איך הוכחנו את משפט השלמות - בנינו מודל מתוך המילון עצמו, על ידי כך שהוספנו קבועים עבור חלק מהפסוקים והמודל שלנו הורכב ממחלקות שקילות של הקבועים הללו. הפרטים המדוייקים אינם קריטיים כרגע, אלא רק העובדה שזה אומר שהמודל שבנינו היה <strong>בן מניה</strong>. הנה המסקנה: לתורה עם מילון בן מניה תמיד קיים מודל בן מניה. התוצאה הזו היא חלק ממה שנקרא <strong>משפט לוונהיים-סקולם</strong>; התוצאה הכללית יותר, שלא אוכיח את כולה כרגע, אומרת שאם יש לתורה מודל אינסופי, אז יש לה מודל <strong>מכל עוצמה אפשרית</strong>. הנה אנחנו רואים עוד "חולשה" של לוגיקה מסדר ראשון - תורות לא יכולות "להכריח" את המודלים שלהם להיות מעוצמה אינסופית ספציפית. מה שכן נכון הוא שהן יכולות לדרוש מהמודלים שלהן להיות מעוצמה <strong>סופית</strong> ספציפית. לא קשה לכתוב פסוק שאומר "קיימים 37 משתנים והערך של כולם שונה זה מזה ולכל משתנה אחר, הערך שלו שווה לאחד מהם". זה יהיה פסוק ארוך למדי (לא <strong>יותר </strong>מדי)<strong> </strong>אבל מכיוון ש-37 הוא מספר סופי, הוא יהיה סופי באורכו ולכן חוקי, וכל מודל שמספק את הפסוק הזה יהיה בן 37 איברים בדיוק.

משפט לוונהיים-סקולם הוא מעניין ושימושי בהקשרים רבים, אבל כרגע אני רוצה רק לתת טעימה לאחת מהמסקנות שלו, שגם לה ראוי להקדיש פוסט נפרד ורציני יותר - <strong>פרדוקס סקולם</strong>. אם עד עכשיו הדברים שהצגתי נראו לי מוזרים בהתחלה אבל קלים יחסית לעיכול, פרדוקס סקולם הוא בהחלט משהו שעד היום אני מרגיש לא בנוח לכתוב עליו מרוב שהוא מרגיש לי מוזר.

הנה הפרדוקס: אנחנו מניחים שתורת הקבוצות האקסיומטית, בניסוח של צרמלו-פרנקל, היא עקבית. עד כאן אין בעיה. אם היא עקבית, קיים לה מודל; בפרט המודל הזה חייב להיות אינסופי (האקסיומות של צרמלו-פרנקל חזקות מספיק כדי להבטיח אינסוף איברים שונים זה מזה). מכאן שעל פי לוונהיים-סקולם, יש מודל בן מניה לתורת הקבוצות האקסיומטית. כלומר, מודל שבו <strong>העולם כולו</strong> מכיל רק מספר בן מניה של איברים, ועדיין מקיים את <strong>כל</strong> המשפטים שנובעים מצרמלו-פרנקל. אבל אחד מהמשפטים הללו הוא האלכסון המפורסם של קנטור שמוכיח שקיימות קבוצות לא בנות מניה. אבל איך קבוצה בת מניה יכולה להתקיים כחלק ממודל שבו יש רק מספר בן מניה של איברים בסך הכל? אין לה "מאיפה" לקחת את האיברים הללו חוץ מאשר העולם של המודל; אין מנוס, השורה התחתונה היא שכל קבוצה במודל הזה היא עצמה בת מניה, וזאת למרות שצרמלו-פרנקל מוכיח שיש קבוצות לא בנות מניה. האם הגענו לסתירה בצרמלו-פרנקל וכל תורת הקבוצות קורסת?

אתם בוודאי מנחשים ששום דבר לא קורה והמתמטיקה ניצלה מחורבן, אבל <strong>למה</strong>? על פניו אין שום פגם כאן. אולי האלכסון של קנטור שגוי...? אבל לא, זה הרי משפט כל כך פשוט! אז מה השתבש?

התשובה היא עדינה ומבלבלת למדי ומצריכה מאיתנו להיזכר מחדש בהגדרות. "קבוצה בת מניה" היא קבוצה שקיימת פונקציה חד-חד-ערכית ועל מהטבעיים אליה. עכשיו, מה שהאלכסון של קנטור מוכיח הוא <strong>לא</strong> את הטענה "קיימת קבוצה לא בת מניה" אלא את הטענה "קיימת <strong>במודל שלנו </strong>קבוצה שלא קיימת <strong>במודל שלנו</strong> פונקציה חד-חד-ערכית ועל מהטבעיים אליה". חשוב לזכור שפונקציות הן בבסיסן בסך הכל קבוצות - קבוצות של זוגות סדורים של קלט ופלט - והמודל בן המניה של צרמלו-פרנקל כנראה נראה "מוזר" מלכתחילה; בפרט, אין שום סיבה להניח שקבוצות שאנו לוקחים את קיומן כמובן מאליו בדרך כלל אכן יהיו קיימות בו.

במילים אחרות, במודל הבן מניה הקבוצה ה"לא בת מניה" באמת תהיה בת מניה; אבל מבחינת המודל הזה אין שום דרך להבחין בכך כי הפונקציה שמוכיחה זאת אינה קיימת במודל. מבלבל? ללא ספק. בעייתי מבחינה פילוסופית? ייתכן; פוסט נפרד על הפרדוקס יהיה חייב להתייחס להיבטים הפילוסופיים. בעיה מבחינה מתמטית? לא ולא. פשוט תוצאה מוזרה מאוד במבט ראשון. לא באמת פרדוקס במובן המלא של המילה, כמו פרדוקס ראסל.

אם כן, אלו היו מספר דוגמאות לתוצאות המפתיעות מאוד של משפט השלמות, וכדאי לזכור שאלו התוצאות ה<strong>מיידיות</strong>, שאפשר לתאר בחטף בפוסט כמו זה, ושבהמשך תורת המודלים יש תוצאות מוזרות אף יותר. אני מקווה שזה לכשעצמו משכנע אתכם עד כמה לוגיקה מתמטית יכולה להיות תחום מגניב.